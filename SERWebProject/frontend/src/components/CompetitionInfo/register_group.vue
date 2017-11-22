<template>
  <el-dialog @close="closeDialog" title="加入队员" :visible.sync="groupDialogFormVisible">
    <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="100px" class="demo-dynamic">
      <el-form-item
        prop="name"
        label="队长姓名"
        :rules="[
          { required: true, message: '请输入隊長姓名', trigger: 'blur' },
          { min: 2, max: 5, message: '长度在 2 到 5 个字符', trigger: 'blur' }
        ]"
      >
        <el-input style="width: 70%;" v-model="dynamicValidateForm.name"></el-input>
      </el-form-item>
      <el-form-item
        v-for="(teamate, index) in dynamicValidateForm.teamates"
        :label="'队员 ' + (index+1)"
        :key="teamate.key"
        :prop="'teamates.' + index + '.value'"
        :rules="[
        {required: true, message: '队员不能为空', trigger: 'blur'},
        { min: 2, max: 5, message: '长度在 2 到 5 个字符', trigger: 'blur' }
        ]"
      >
        <el-input style="width: 50%;" v-model="teamate.value"></el-input>
        <el-button style="width: 20%;" @click.prevent="checkteamate()">确认</el-button>
        <el-button style="width: 20%;" @click.prevent="removeteamate(teamate)">删除</el-button>
      </el-form-item>
      <el-form-item>
        <el-button @click="addteamate('dynamicValidateForm')">新增一名队友</el-button>
        <br><br>
        <el-button type="primary" @click="open2">提交</el-button>
        <el-button @click="resetForm('dynamicValidateForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>
<script>
export default {
  props: {
    groupDialogFormVisible: {
      type: Boolean,
      default: false
    },
    pid: {
      default: ''
    },
    uid: {
      default: ''
    }
  },
  data () {
    return {
      dynamicValidateForm: {
        teamates: [{
          value: ''
        }],
        name: ''
      },
      registerForm: {
        name: ''
      },
      user_pk: '',
      ruleForm: {
        faculty: '',
        name: '',
        gender: '',
        id_card: '',
        student_id: '',
        birth_date: '',
        clothes_size: '',
        cellphone_num: ''
      },
      formLabelWidth: '120px'
    }
  },
  created: function () {
    this.user_info_request(this.uid)
  },
  methods: {
    submitForm (formName) {
      this.$http.post('http://111.230.226.45:8888/api/set_teammate_confirm/' + this.uid + '/' + this.pid)
      this.$emit('finishGroup')
    },
    open2 () {
      this.$msgbox({
        title: '消息',
        message: '确认后无法取消',
        showCancelButton: true,
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        beforeClose: (action, instance, done) => {
          if (action === 'confirm') {
            this.submitForm(this.dynamicValidateForm)
            this.closeDialog()
            done()
          } else {
            done()
          }
        }
      }).then(action => {
        this.$message({
          type: 'info',
          message: '成功提交'
        })
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    removeteamate (item) {
      var index = this.dynamicValidateForm.teamates.indexOf(item)
      if (index !== -1) {
        this.dynamicValidateForm.teamates.splice(index, 1)
      }
    },
    addteamate (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.dynamicValidateForm.teamates.push({
            value: '',
            key: Date.now()
          })
        } else {
          console.log('error')
        }
      })
    },
    checkteamate () {
      var i = this.dynamicValidateForm.teamates.length - 1
      this.registerForm.name = this.dynamicValidateForm.teamates[i].value
      this.$http.post('http://111.230.226.45:8888/api/add_teammate/' + this.uid + '/' + this.pid, this.registerForm, {emulateJSON: true}).then((response) => {
        var res = JSON.parse(response.bodyText)
        if (res.status !== 0) {
          alert('User doesn\'t exsist !')
        } else {
          alert('confirm !')
        }
      })
    },
    user_info_request (username) {
      this.$http.get('http://111.230.226.45:8888/api/user_info_request/' + username).then((response) => {
        var res = JSON.parse(response.bodyText)
        if (res.error_num === 0) {
          this.dynamicValidateForm.name = res.list[0].fields.name
          this.ruleForm.birth_date = ''
          this.user_pk = res.list[0].pk
        } else {
          this.$message.error('获取项目列表失败"')
          console.log(res['msg'])
        }
      })
    },
    closeDialog () {
      this.$emit('finishGroup')
    }
  }
}
</script>
<style scoped>
  .el-button{
    margin: 5px;
  }
</style>

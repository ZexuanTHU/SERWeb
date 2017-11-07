<template>
  <el-dialog title="團隊報名" :visible.sync="dialogFormVisible">
    <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="100px" class="demo-dynamic">
      <el-form-item
        prop="name"
        label="隊長姓名"
        :rules="[
          { required: true, message: '请输入隊長姓名', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
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
        { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ]"
      >
        <el-input style="width: 70%;" v-model="teamate.value"></el-input>
        <el-button style="width: 20%;" @click.prevent="removeteamate(teamate)">删除</el-button>
      </el-form-item>
      <el-form-item>
        <el-button @click="addteamate('dynamicValidateForm')">新增队友</el-button>
        <el-button type="primary" @click="submitForm('dynamicValidateForm')">提交</el-button>
        <el-button @click="resetForm('dynamicValidateForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>
<script>
export default {
  props: {
    dialogFormVisible: {
      type: Boolean,
      default: false
    },
    projectpk: {
      type: String,
      default: ''
    },
    uid: {
      type: String,
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
    this.user_info_request('skyrealmz')
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          console.log('error submit!!')
          return false
        }
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
    user_info_request (username) {
      this.$http.get('http://127.0.0.1:8000/api/user_info_request?username=' + username).then((response) => {
        var res = JSON.parse(response.bodyText)
        console.log(res)
        if (res.error_num === 0) {
          this.dynamicValidateForm.name = res.list[0].fields.name
          this.ruleForm.birth_date = ''
          this.user_pk = res.list[0].pk
        } else {
          this.$message.error('获取项目列表失败"')
          console.log(res['msg'])
        }
      })
    }
  }
}
</script>
<style scoped>
  .el-button{
    margin: 5px;
  }
</style>
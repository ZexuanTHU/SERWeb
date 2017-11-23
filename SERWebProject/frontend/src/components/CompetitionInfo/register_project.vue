<template>
  <el-dialog @close="closeDialog" title="报名资料确认" :visible.sync="dialogFormVisible">
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item v-if="this.group === true" label="队名" prop="teamname">
          <el-input v-model="ruleForm.teamname"></el-input>
        </el-form-item>
        <h4 v-if="this.group === true">队长资料确认</h4>
        <el-form-item label="院系" prop="faculty">
          <el-select v-model="ruleForm.faculty" placeholder="选择院系">
            <el-option label="计算机" value="CS"></el-option>
            <el-option label="自动化" value="AUTO"></el-option>
            <el-option label="电子" value="EE"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="名字" prop="name">
          <el-input v-model="ruleForm.name"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="gender">
          <el-select v-model="ruleForm.gender" placeholder="选择性别">
            <el-option label="男" value="M"></el-option>
            <el-option label="女" value="F"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="证件号码" prop="id_card">
          <el-input v-model="ruleForm.id_card"></el-input>
        </el-form-item>
        <el-form-item label="学号" prop="student_id">
          <el-input v-model="ruleForm.student_id"></el-input>
        </el-form-item>
        <el-form-item label="生日" prop="birth_date">
          <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.birth_date" style="width: 100%;"></el-date-picker>
        </el-form-item>
        <el-form-item label="服装号码" prop="clothes_size">
          <el-select v-model="ruleForm.clothes_size" placeholder="选择号码">
            <el-option label="S" value="S"></el-option>
            <el-option label="M" value="M"></el-option>
            <el-option label="L" value="L"></el-option>
            <el-option label="XL" value="XL"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="移动电话" prop="cellphone_num">
          <el-input v-model="ruleForm.cellphone_num"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button v-if="group===true" type="primary" @click="submitForm('ruleForm')">建立队伍</el-button>
          <el-button v-else type="primary" @click="submitForm('ruleForm')">报名</el-button>
          <el-button @click="resetForm('ruleForm')">重置</el-button>
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
    pid: {
      default: ''
    },
    uid: {
      default: ''
    },
    group: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      user_pk: '',
      ruleForm: {
        faculty: '',
        name: '',
        gender: '',
        id_card: '',
        student_id: '',
        birth_date: '',
        clothes_size: '',
        cellphone_num: '',
        teamname: ''
      },
      registerForm: {
        user_id: '',
        project_id: ''
      },
      groupForm: {
        group_name: ''
      },
      rules: {
        teamname: [
          { required: true, message: '请填队名', trigger: 'blur' }
        ],
        faculty: [
          { required: true, message: '请选择院系', trigger: 'change' }
        ],
        name: [
          { required: true, message: '请输入名字', trigger: 'blur' },
          { min: 2, max: 20, message: '长度在 2 到 20 个字符', trigger: 'blur' }
        ],
        gender: [
          { required: true, message: '请选性别', trigger: 'change' }
        ],
        id_card: [
          { required: true, message: '请输入身份证号码', trigger: 'blur' },
          { min: 0, max: 30, message: '长度在 0 到 30 个字符', trigger: 'blur' }
        ],
        student_id: [
          { required: true, message: '请输入学号', trigger: 'blur' },
          { legth: 10, message: '长度10个字符', trigger: 'blur' }
        ],
        clothes_size: [
          { required: true, message: '请选择衣服号码', trigger: 'change' }
        ],
        cellphone_num: [
          { required: true, message: '请输入学号', trigger: 'blur' },
          { min: 11, max: 11, message: '长度12个字符', trigger: 'blur' }
        ]
      },
      formLabelWidth: '120px'
    }
  },
  created: function () {
    this.user_info_request(this.uid)
  },
  methods: {
    user_info_request (uid) {
      this.$http.get('http://111.230.226.45:8888/api/user_info_request/' + uid).then((response) => {
        var res = JSON.parse(response.bodyText)
        if (res.error_num === 0) {
          this.ruleForm = res.list[0].fields
          this.user_pk = res.list[0].pk
          this.ruleForm.birth_date = this.ruleForm.birth_date + 'T00:00:00.000Z'
        } else {
          this.$message.error('获取项目列表失败"')
          console.log(res['msg'])
        }
      })
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.registerForm.user_id = this.uid
          this.registerForm.project_id = this.pid
          if (this.group === false) {
            this.$http.post('http://111.230.226.45:8888/api/project_register/' + this.uid + '/' + this.pid).then((response) => {
              var res = JSON.parse(response.bodyText)
              if (res.error_num === 0) {
                this.$message({message: '报名成功', type: 'success'})
              }
              if (res.error_num === 1) {
                this.$message({message: '抱歉，出错了！', type: 'warning'})
              }
              if (res.error_num === 2) {
                this.$message({message: '项目或个人资料出错', type: 'warning'})
              }
              if (res.error_num === 3) {
                this.$message({message: '已达最高报名人数', type: 'warning'})
              }
              if (res.error_num === 4) {
                this.$message({message: '您已在报名列表里', type: 'warning'})
              }
            })
            this.dialogFormVisible = false
            this.closeDialog()
          } else {
            this.groupForm.group_name = this.ruleForm.teamname
            this.$http.post('http://111.230.226.45:8888/api/add_group/' + this.uid + '/' + this.pid, this.groupForm, {emulateJSON: true}).then((response) => {
              this.dialogFormVisible = false
              var res = JSON.parse(response.bodyText)
              if (res.error_num === 0) {
                this.$message({message: '创建成功', type: 'success'})
                this.$emit('finish')
              }
              if (res.error_num === 1) {
                this.$message({message: '抱歉，出错了！', type: 'warning'})
                this.$emit('error')
              }
              if (res.error_num === 2) {
                this.$message({message: '项目或个人资料出错', type: 'warning'})
                this.$emit('error')
              }
              if (res.error_num === 3) {
                this.$message({message: '已达最高报名人数', type: 'warning'})
                this.$emit('error')
              }
              if (res.error_num === 4) {
                this.$message({message: '您已在报名列表里', type: 'warning'})
                this.$emit('error')
              }
            })
          }
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    closeDialog () {
      this.$emit('dialogStatus', false)
    }
  }
}
</script>

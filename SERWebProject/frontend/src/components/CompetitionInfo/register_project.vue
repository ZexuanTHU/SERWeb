<template>
  <el-dialog @open="checkGroup" @close="closeDialog" title="报名资料确认" :visible.sync="dialogFormVisible">
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
        <el-form-item prop="birth_date">
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
          <el-button type="primary" @click="submitForm('ruleForm')">{{groupStatus}}</el-button>
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
      type: String,
      default: ''
    },
    uid: {
      type: String,
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
      groupStatus: '',
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
          { min: 2, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        gender: [
          { required: true, message: '请选性别', trigger: 'change' }
        ],
        id_card: [
          { required: true, message: '请输入身份证号码', trigger: 'blur' },
          { min: 0, max: 20, message: '长度在 x 到 x 个字符', trigger: 'blur' }
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
      console.log(this.group)
      if (this.group === true) {
        this.groupStatus = '建立队伍'
      } else {
        this.groupStatus = '报名'
      }
      this.$http.get('http://127.0.0.1:8000/api/user_info_request/' + uid).then((response) => {
        var res = JSON.parse(response.bodyText)
        console.log(res)
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
          console.log(this.registerForm)
          if (this.group === false) {
            this.$http.post('http://127.0.0.1:8000/api/project_register/' + this.uid + '/' + this.pid)
            this.dialogFormVisible = false
            this.closeDialog()
            alert('報名成功')
          } else {
            this.groupForm.group_name = this.ruleForm.teamname
            this.$http.post('http://127.0.0.1:8000/api/add_group/' + this.uid + '/' + this.pid, this.groupForm, {emulateJSON: true}).then((response) => {
              this.dialogFormVisible = false
              alert('创建成功')
              this.$emit('finish')
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
    },
    checkGroup () {
      if (this.group === true) {
        this.groupStatus = '建立队伍'
      } else {
        this.groupStatus = '报名'
      }
    }
  }
}
</script>

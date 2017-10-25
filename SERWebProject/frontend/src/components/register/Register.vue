<template>
  <el-form :model="registerForm" :rules="registerRules" ref="registerForm" label-width="120px" id="login">
    <el-form-item prop="username">
      <el-input placeholder="Username" v-model="registerForm.username" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item prop="email">
      <el-input placeholder="E-mail" type="email" v-model="registerForm.email" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item prop="pass">
      <el-input placeholder="Password" type="password" v-model="registerForm.pass" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item prop="checkpass">
      <el-input placeholder="Check Password" type="password" v-model="registerForm.checkPass"
                auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="register('registerForm')">Register</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
  export default {
    data () {
      var validateUsername = (rule, value, callback) => {
        var pattern = /^[\w\u4e00-\u9fa5]{3,10}$/g
        if (value === '') {
          callback(new Error('请输入用户名'))
        } else if (!pattern.test(value)) {
          callback(new Error('请输入3-10个字母/汉字/数字/下划线'))
        } else {
          callback()
        }
      }
      var validateEmail = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入邮箱'))
        }
      }
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'))
        } else {
          if (this.registerForm.checkPass !== '') {
            this.$refs.registerForm.validateField('checkPass')
          }
          callback()
        }
      }
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'))
        } else if (value !== this.registerForm.pass) {
          callback(new Error('两次输入密码不一致!'))
        } else {
          callback()
        }
      }
      return {
        registerForm: {
          username: '',
          email: '',
          pass: '',
          checkPass: ''
        },
        registerRules: {
          username: [
            {validator: validateUsername, trigger: 'blur'}
          ],
          email: [
            {validator: validateEmail, trigger: 'blur'}
          ],
          pass: [
            {validator: validatePass, trigger: 'blur'}
          ],
          checkPass: [
            {validator: validatePass2, trigger: 'blur'}
          ]
        }
      }
    },
    methods: {
      register (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!')
            this.$http.post('http://127.0.0.1:8000/api/register', this.registerForm)
          } else {
            console.log('error submit!!')
            return false
          }
        })
      }
    }
  }
</script>

<style scoped>
  @import url("//unpkg.com/element-ui@1.4.7/lib/theme-default/index.css");

  #login {
    max-width: 350px;
    margin: auto;
    padding: 50px;
    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
  }

  .el-form-item {
    margin-left: -120px;
  }

  .el-button {
    width: 100%;
  }

</style>

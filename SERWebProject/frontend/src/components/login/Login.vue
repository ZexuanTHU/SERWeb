<template>
    <el-form :model="loginForm" :rules="loginRules" ref="loginForm" label-width="120px" id="login">
      <el-form-item  prop="username">
        <el-input placeholder="Account9 用户名"  v-model="loginForm.username" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item prop="pass">
        <el-input placeholder="Account9 密码" type="password" v-model="loginForm.pass" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('loginForm')">登录</el-button>
      </el-form-item>
      <el-button>
        <router-link to="Register">新用户认证</router-link>
      </el-button>
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
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'))
        } else {
          if (this.loginForm.checkPass !== '') {
            this.$refs.loginForm.validateField('checkPass')
          }
          callback()
        }
      }

      return {
        loginForm: {
          username: '',
          pass: ''
        },
        loginRules: {
          username: [
            { validator: validateUsername, trigger: 'blur' }
          ],
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ]
        }
      }
    },
    methods: {
      submitForm (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!')
            this.$http.post('http://localhost:8000/api/users', formName)
                .then((response) => {
                  alert('login')
                }
              )
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

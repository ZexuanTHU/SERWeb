<template>
    <el-form :model="loginForm" :rules="loginRules" ref="loginForm" label-width="120px" id="login">
      <el-form-item  prop="username">
        <el-input placeholder="Account9 用户名"  v-model="loginForm.username" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input placeholder="Account9 密码" type="password" v-model="loginForm.password" auto-complete="off"></el-input>
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
//        var pattern = /^[\w\u4e00-\u9fa5]{3,10}!$/g
        if (value === '') {
          callback(new Error('请输入用户名'))
        } else {
          callback()
        }
      }
      var validatePassword = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'))
        } else {
          callback()
        }
      }

      return {
        loginForm: {
          username: '',
          password: ''
        },
        loginRules: {
          username: [
            { validator: validateUsername, trigger: 'blur' }
          ],
          password: [
            { validator: validatePassword, trigger: 'blur' }
          ]
        }
      }
    },
    methods: {
      submitForm (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            let username = this.loginForm.username
            let password = this.loginForm.password
            this.$http.get('http://111.230.226.45:8888/api/login?username=' + username + '&password=' + password)
                .then((response) => {
                  let res = JSON.parse(response.bodyText)
                  if (res.status === 0) {
                    alert('登录成功，返回首页')
                    this.$router.push('/')
                  } else {
                    alert('登录失败，请检查您输入的用户名与密码')
                  }
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

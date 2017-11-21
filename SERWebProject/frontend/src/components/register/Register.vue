<template>
  <el-form :model="registerForm" :rules="registerRules" ref="registerForm" label-width="120px" id="login">
    <el-form-item prop="username">
      <el-input placeholder="Account9 用户名" v-model="registerForm.username" auto-complete="off"></el-input>
    </el-form-item>
    <!--<el-form-item prop="email">
      <el-input placeholder="E-mail" type="email" v-model="registerForm.email" auto-complete="off"></el-input>
    </el-form-item>-->
    <el-form-item prop="pass">
      <el-input placeholder="Account9 密码" type="password" v-model="registerForm.pass" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item prop="checkPass">
      <el-input placeholder="请再次确认 Account9 密码" type="password" v-model="registerForm.checkPass"
                auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="register('registerForm')">认证</el-button>
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
            let clientid = 'EqlnQKv2oxvF2imyZloL6N1Doy8'
            let clientsecret = 'bmKP9oZbal6W6qSNbZtj'
            let uname = this.registerForm.username
//            let email = this.registerForm.email
            let pwd = this.registerForm.pass
            this.$http.get('https://accounts.net9.org/api/access_token?client_id=' + clientid +
              '&client_secret=' + clientsecret +
              '&username=' + this.registerForm.username +
              '&password=' + this.registerForm.pass)
              .then((response) => {
                let res = JSON.parse(response.bodyText)
                if (res.error) {
                  alert('登录失败！请输入正确的 Account9 用户名及密码')
                } else {
                  console.log(res)
                  this.$http.get('https://accounts.net9.org/api/userinfo?access_token=' + res.access_token)
                    .then((response) => {
                      let res2 = JSON.parse(response.bodyText)
                      console.log(res2)
                      this.$http.get('http://111.230.226.45:8888/api/register?username=' + uname +
//                        '&email=' + email +
                        '&password1=' + pwd +
                        '&password2=' + pwd)
                      alert('认证成功！')
                      alert('你今后可以直接使用 Account9 账户登录 SERWeb 体育赛事报名平台！')
                      this.$router.push('Login')
                    })
                }
              })
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

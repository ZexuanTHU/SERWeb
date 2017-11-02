<!--主界面上未使用此模板-->
<template>
  <div id="nav">
    <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">
        <router-link to="./">首页</router-link>
      </el-menu-item>
      <!--<el-submenu index="2">
        <template slot="title">项目列表</template>
        <el-menu-item index="2-1">项目报名</el-menu-item>
        <el-menu-item index="2-2">比赛日程</el-menu-item>
      </el-submenu>-->
      <el-menu-item index="2">赛事信息</el-menu-item>
      <el-menu-item index="3">酒井名人堂</el-menu-item>
      <el-menu-item index="4">系代表队宣传</el-menu-item>
      <el-submenu class="user" index="5" v-if="user.authenticated">
        <template slot="title">this.loginForm.username</template>
        <el-menu-item index="5-1">
          <router-link to="userpage">用户信息</router-link>
        </el-menu-item>
        <el-menu-item index="5-2" @click="logout()">登出</el-menu-item>
      </el-submenu>
      <el-menu-item class="user" index="5">
        <!--<router-link to="Login">登录/新用户认证</router-link>-->
        <el-button type="text" @click="dialogVisible = true" v-if="!user.authenticated">登录/新用户认证</el-button>

        <el-dialog
          :visible.sync="dialogVisible"
          size="tiny"
          :before-close="handleClose">
          <el-form :model="loginForm" :rules="loginRules" ref="loginForm" label-width="120px" class="login">
            <el-form-item prop="username">
              <el-input placeholder="Account9 用户名" v-model="loginForm.username" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item prop="password">
              <el-input placeholder="Account9 密码" type="password" v-model="loginForm.password"
                        auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm('loginForm')">登录</el-button>
            </el-form-item>

            <el-collapse v-model="activeName2">
              <el-collapse-item title="新用户认证">
                <el-form :model="registerForm" :rules="registerRules" ref="registerForm" label-width="120px"
                         class="login">
                  <el-form-item prop="username">
                    <el-input placeholder="Account9 用户名" v-model="registerForm.username" auto-complete="off"></el-input>
                  </el-form-item>
                  <!--<el-form-item prop="email">
                      <el-input placeholder="E-mail" type="email" v-model="registerForm.email" auto-complete="off"></el-input>
                    </el-form-item>-->
                  <el-form-item prop="pass">
                    <el-input placeholder="Account9 密码" type="password" v-model="registerForm.pass"
                              auto-complete="off"></el-input>
                  </el-form-item>
                  <el-form-item prop="checkPass">
                    <el-input placeholder="请再次确认 Account9 密码" type="password" v-model="registerForm.checkPass"
                              auto-complete="off"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-button type="primary" @click="register('registerForm')">认证</el-button>
                  </el-form-item>
                </el-form>
              </el-collapse-item>
            </el-collapse>
            <!--<el-button  @click="dialogVisible2 = true">新用户认证</el-button>-->
            <!--<router-link to="Register">新用户认证</router-link>-->
          </el-form>
        </el-dialog>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");
  @import url("../css/w3.css");

  a {
    text-decoration: none;
  }
</style>

<script>
  import auth from '../auth'
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
      var validateUsername2 = (rule, value, callback) => {
        var pattern = /^[\w\u4e00-\u9fa5]{3,10}$/g
        if (value === '') {
          callback(new Error('请输入用户名'))
        } else if (!pattern.test(value)) {
          callback(new Error('请输入3-10个字母/汉字/数字/下划线'))
        } else {
          callback()
        }
      }
      var validatePass1 = (rule, value, callback) => {
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
        loginForm: {
          username: '',
          password: ''
        },
        loginRules: {
          username: [
            {validator: validateUsername, trigger: 'blur'}
          ],
          password: [
            {validator: validatePassword, trigger: 'blur'}
          ]
        },
        registerForm: {
          username: '',
          email: '',
          pass: '',
          checkPass: ''
        },
        registerRules: {
          username: [
            {validator: validateUsername2, trigger: 'blur'}
          ],
          pass: [
            {validator: validatePass1, trigger: 'blur'}
          ],
          checkPass: [
            {validator: validatePass2, trigger: 'blur'}
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
            this.$http.get('http://localhost:8000/api/login?username=' + username + '&password=' + password)
              .then((response) => {
                let res = JSON.parse(response.bodyText)
                if (res.status === 0) {
                  alert('登录成功，返回首页')
                  this.dialogVisible = false
//                  this.$router.push('/')
//                  this.user.authenticated = true
                  auth.login(this, this.loginForm, 'userpage')
                } else {
                  alert('登录失败，请检查您输入的用户名与密码')
                }
              })
          } else {
            console.log('error submit!!')
            return false
          }
        })
      },
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
                      this.$http.get('http://localhost:8000/api/register?username=' + uname +
//                        '&email=' + email +
                        '&password1=' + pwd +
                        '&password2=' + pwd)
                      alert('认证成功！')
                      alert('你今后可以直接使用 Account9 账户登录 SERWeb 体育赛事报名平台！')
                      this.activeName2 = 10
//                      this.$router.push('Login')
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

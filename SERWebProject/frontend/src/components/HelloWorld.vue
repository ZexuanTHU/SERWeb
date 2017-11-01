<!-- 温家尊: 添加 auth.js，判断登录状态-->

<template>
  <div>
    <div id="nav">
      <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1"><router-link to="./">首页</router-link></el-menu-item>
        <!--<el-submenu index="2">
          <template slot="title">项目列表</template>
          <el-menu-item index="2-1">项目报名</el-menu-item>
          <el-menu-item index="2-2">比赛日程</el-menu-item>
        </el-submenu>-->
        <el-menu-item index="2">赛事信息</el-menu-item>
        <el-menu-item index="3">酒井名人堂</el-menu-item>
        <el-menu-item index="4">系代表队宣传</el-menu-item>
        <el-menu-item id="user" index="5">
          <!--<router-link to="Login">登录/新用户认证</router-link>-->
          <el-submenu index="6" v-if="user.authenticated">
            <template slot="title">this.loginForm.username</template>
            <el-menu-item index="6-1"><router-link to="userpage">用户信息</router-link></el-menu-item>
            <el-menu-item index="6-2" @click="logout()">登出</el-menu-item>
          </el-submenu>

          <el-button type="text" @click="dialogVisible = true" v-if="!user.authenticated">登录/新用户认证</el-button>

          <el-dialog
            :visible.sync="dialogVisible"
            size="tiny"
            :before-close="handleClose">
            <el-form :model="loginForm" :rules="loginRules" ref="loginForm" label-width="120px" class="login">
              <el-form-item  prop="username">
                <el-input placeholder="Account9 用户名"  v-model="loginForm.username" auto-complete="off"></el-input>
              </el-form-item>
              <el-form-item prop="password">
                <el-input placeholder="Account9 密码" type="password" v-model="loginForm.password" auto-complete="off"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm('loginForm')">登录</el-button>
              </el-form-item>

              <el-collapse v-model="activeName2">
                <el-collapse-item title="新用户认证">
                  <el-form :model="registerForm" :rules="registerRules" ref="registerForm" label-width="120px" class="login">
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
                </el-collapse-item>
              </el-collapse>
                <!--<el-button  @click="dialogVisible2 = true">新用户认证</el-button>-->
                <!--<router-link to="Register">新用户认证</router-link>-->
            </el-form>
          </el-dialog>
        </el-menu-item>
      </el-menu>
    </div>

    <div id="carousel">
      <el-carousel :interval="5000" arrow="always">
        <el-carousel-item v-for="item in 4" :key="item">
          <img src="../assets/slider1.jpg">
        </el-carousel-item>
      </el-carousel>
    </div>

    <div id="hot news">
      <h1 align="left">热门赛事</h1>
      <a href="" target="_blank" id="more">查看更多 ></a>
      <el-row>
        <el-col :span="8" v-for="(o, index) in 2" :key="o" :offset="index > 0 ? 2 : 0">
          <el-card :body-style="{ padding: '0px' }">
            <img src="../assets/card1.jpg" class="image">
            <div style="padding: 14px;">
              <span>清华大学校园马拉松</span>
              <div class="bottom clearfix">
                <time class="time">{{ currentDate }}</time>
                <el-button type="text" class="button">
                  <router-link to="CompetitionInfo">赛事报名</router-link>
                </el-button>
              </div>
            </div>
            <el-progress type="circle" :percentage="0"></el-progress>
          </el-card>
        </el-col>
      </el-row>
    </div>

    <div id="more news">
      <h1 align="left">其他赛事</h1>
      <el-table
        :data="tableData"
        height="200"
        border
        style="width: 100%">
        <el-table-column
          prop="event"
          label="赛事名称"
          sortable
          align="center">
        </el-table-column>
        <el-table-column
          prop="time"
          label="时间"
          align="center">
        </el-table-column>
        <el-table-column
          prop="host"
          label="主办单位"
          align="center">
        </el-table-column>
        <el-table-column
          prop="type"
          label="种类"
          align="center">
        </el-table-column>
        <el-table-column
          prop="tag"
          label="Tag"
          align="center"
          :filters="[{ text: '已报名', value: '已报名' }, { text: '还没报名', value: '立即报名' }]"
          :filter-method="filterTag"
          filter-placement="bottom-end">
          <template scope="scope">
            <el-tag
              :type="scope.row.tag === 'Home' ? 'primary' : 'success'"
              close-transition>{{scope.row.tag}}</el-tag>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <br/>

    <div id="statistics">
      <div class="container">
        <el-progress type="circle" :percentage="0"></el-progress><h1>event1</h1>
      </div>
      <div class="container">
        <el-progress type="circle" :percentage="25"></el-progress><h1>event2</h1>
      </div>
      <div class="container">
        <el-progress type="circle" :percentage="50"></el-progress><h1>event3</h1>
      </div>
      <div class="container">
        <el-progress type="circle" :percentage="100"></el-progress><h1>event4</h1>
      </div>

    </div>
  </div>
</template>


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
        user: auth.user,
        dialogVisible: false,
        dialogVisible2: false,
        activeIndex: '1',
        activeIndex2: '1',
        activeName: 'first',
        activeName2: '10',
        currentDate: new Date(),
        tableData: [{
          event: 'event',
          time: '111',
          host: '学生会',
          type: '篮球',
          tag: '立即报名'
        }, {
          event: 'event',
          time: '111',
          host: '学生会',
          type: '篮球',
          tag: '立即报名'
        }, {
          event: 'event',
          time: '111',
          host: '学生会',
          type: '篮球',
          tag: '立即报名'
        }, {
          event: 'event',
          time: '111',
          host: '学生会',
          type: '篮球',
          tag: '立即报名'
        }],
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
      logout () {
        auth.logout()
      },
      handleClose (done) {
        done()
      },
      handleSelect (key, keyPath) {
        console.log(key, keyPath)
      },
      handleClick (tab, event) {
        console.log(tab, event)
      },
      formatter (row, column) {
        return row.address
      },
      filterTag (value, row) {
        return row.tag === value
      },
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");

  a {
    text-decoration: none;
  }

  #user {
    float: right;
  }

  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  #hot {
    margin-top: 10px;
    margin-bottom: 20px;
  }

  #more {
    float: right;
    font-size: 12px;
    font-family: sans-serif;
    color: #999999;
    margin-right: 22px;
  }

  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }

  #statistics {
    display: flex;
  }

  .container {
    width: calc(100% / 4);
    height: 150px;
    padding: 0;
    margin: 0;
    float: left;
  }

  .login {
    max-width: 350px;
    margin: auto;
    padding: 50px;
    /*box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);*/
  }

  .el-form-item {
    margin-left: -120px;
  }

  .el-button {
    width: 100%;
  }
</style>

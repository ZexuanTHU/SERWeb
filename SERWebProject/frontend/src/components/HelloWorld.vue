<template>
  <div>
    <mheader></mheader>
    <div id="carousel" align="center" style="margin-bottom: 50px">
      <el-carousel :interval="5000" type="card" height="500px">
        <el-carousel-item v-for="pic in pics" :key="pic" style="height: 500px">
          <img :src="getImage(pic)" v-bind:alt="pic" style="height: 100%; width: 100%">
        </el-carousel-item>
      </el-carousel>
    </div>

    <div id="hot news" style="margin-left: 5%; margin-right: 5%">
      <h1 align="left">热门赛事</h1>
      <a href="" target="_blank" id="more" style="margin-right: 50px">查看更多 ></a>
      <br/>
      <el-row>
        <el-col :span="8" v-for="field in hot_project_card" :key="field.id">
          <el-card :body-style="{ padding: '0px' }"  style="margin-right: 50px">
            <img src="../assets/card1.jpg" class="image">
            <div style="padding: 14px;">
              <p>{{ field.fields.project_name }}</p>
            </div>
            <div style="width: 100%; position: relative; overflow: hidden">
              <div style="width: 100px; float: left">
                <el-progress type="circle" :percentage="field.fields.project_hot/field.fields.max_reg*100" style="margin-left: 10%; margin-bottom: 5%"></el-progress></div>
              <div  style="position: absolute; bottom: 0; right: 0; margin-bottom: 5%; margin-right: 5%">
                <router-link :to="{name: 'CompetitionInfo', params: {pk: field.pk}}">
                  <el-button type="primary" style="width: 150px">
                    <p style="color: white">赛事详情</p>
                  </el-button>
                </router-link>
              </div>
              <div style="position: absolute; bottom: 0; right: 100px; margin-bottom: 5%; margin-right: 20%">
                <el-button style="width: 150px">
                  <p>一键报名</p>
                </el-button>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>

    <div id="more news"  style="margin-left: 5%; margin-right: 5%">
      <h1 align="left">其他赛事</h1>
      <el-table
        :data="latest_project_list"
        height="600"
        border
        style="width: 100%">
        <el-table-column
          prop="project_name"
          label="赛事名称"
          align="center">
          <template scope="scope"> {{ scope.row.fields.project_name }} </template>
        </el-table-column>
        <el-table-column
          prop="project_text"
          label="赛事简介"
          align="center">
          <template scope="scope"> {{ scope.row.fields.project_text }} </template>
        </el-table-column>
        <el-table-column
          prop="date"
          label="报名起止时间"
          align="center">
          <template scope="scope"> {{ scope.row.fields.pub_date }} -- {{ scope.row.fields.ddl_date }} </template>
        </el-table-column>
        <el-table-column
          prop="project_hot"
          label="当前报名人数"
          align="center">
          <template scope="scope"> {{ scope.row.fields.project_hot }} </template>
        </el-table-column>
        <el-table-column
          prop="max_reg"
          label="报名人数限制"
          align="center">
          <template scope="scope"> {{ scope.row.fields.max_reg }} </template>
        </el-table-column>
        <el-table-column
          prop="contact_name"
          label="紧急联系人姓名"
          align="center">
          <template scope="scope"> {{ scope.row.fields.contact_name }} </template>
        </el-table-column>
        <el-table-column
          prop="contact_tel"
          label="紧急联系人电话"
          align="center">
          <template scope="scope"> {{ scope.row.fields.contact_tel }} </template>
        </el-table-column>
        <el-table-column
          prop="register"
          label="赛事报名"
          align="center">
          <template scope="scope">
            <el-button  size="mini">
              <p>一键报名</p>
            </el-button>
            <router-link :to="{name: 'CompetitionInfo', params: {pk: scope.row.pk}}">
              <el-button type="primary" size="mini">
                <p style="color: white">赛事详情</p>
              </el-button>
            </router-link>

          </template>
        </el-table-column>
      </el-table>
    </div>

    <br/>
  </div>
</template>


<script>
  import auth from '../auth'
  import mheader from './header.vue'

  export default {
    data () {
      return {
        pics: [
          'slider1',
          'slider2',
          'card1'
        ],
        hot_project_card: [{
          fields: [{
            project_name: '',
            project_hot: '',
            max_reg: ''
          }],
          pk: '',
          model: ''
        }],
        latest_project_list: [{
          fields: [{
            project_name: '',
            project_text: '',
            project_hot: '',
            ddl_date: '',
            pub_date: '',
            max_reg: '',
            contact_name: '',
            contact_tel: ''
          }],
          pk: ''
        }]
      }
    },
    created: function () {
      this.project_list_display()
      this.project_card_display()
    },
    methods: {
      getImage (index) {
        var images = require.context('../assets/', false, /\.jpg$/)
        return images('./' + index + '.jpg')
      },
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
      },
      project_list_display () {
        this.$http.get('http://127.0.0.1:8000/api/project_list_display').then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.latest_project_list = res['list']
          } else {
            this.$message.error('获取项目列表失败"')
            console.log(res['msg'])
          }
        })
      },
      project_card_display () {
        this.$http.get('http://127.0.0.1:8000/api/project_card_display').then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.hot_project_card = res['list']
          } else {
            this.$message.error('获取项目列表失败"')
            console.log(res['msg'])
          }
        })
      }
    },
    components: {
      'mheader': mheader
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");

  a {
    text-decoration: none;
  }

  .user {
    float: right;
  }

  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
  }

  .el-carousel__item:nth-child(n) {
    background-color: #99a9bf;
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
</style>

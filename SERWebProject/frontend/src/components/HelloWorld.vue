<template>
  <div>
    <mheader ref="header"></mheader>
    <!--<div id="carousel" style="margin-bottom: 50px">-->
      <!--<el-carousel :interval="5000" type="card" height="500px">-->
        <!--<el-carousel-item v-for="pic in pics" :key="pic" align="center">-->
          <!--<img :src="getImage(pic)" v-bind:alt="pic" style="max-height: 90%; width:100%">-->
          <!--<p>test</p>-->
        <!--</el-carousel-item>-->
      <!--</el-carousel>-->
    <!--</div>-->

    <div id="carousel" style="margin-bottom: 50px">
      <el-carousel :interval="5000" type="card" height="500px">
        <el-carousel-item v-for="img in carousel_img" :key="img" align="center">
          <img :src="getImage(img.fields.carousel_image)" v-bind:alt="img" style="max-height: 90%; width:100%">
          <p> {{ img.fields.carousel_mark }} </p>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div id="hot news" style="margin-left: 5%; margin-right: 5%">
      <h1 align="left">热门赛事</h1>
      <!--<a href="" target="_blank" id="more">查看更多 ></a>-->
      <br/>
      <el-row>
        <el-col :span="8" v-for="field in hot_project_card" :key="field.id">
          <el-card :body-style="{ padding: '0px' }" style="margin-right: 5%">
            <img src="../assets/card1.jpg" class="image">
            <div id="container">
              <div style="float: left">
                <div id="left-top" style="width: 250px; padding-left: 14px; padding-top: 14px">
                  <h3> {{ field.fields.project_name }} </h3>
                </div>
                <div id="left-bottom" style="width: 250px; padding-left: 14px; padding-top: 30px">
                  <el-button @click="oneclick(field.pk)" >
                    <p style="color: black">一键报名</p>
                  </el-button>
                  <!--<router-link :to="{name: 'project', params: {uid:$route.params.uid, pid: field.pk}}">-->
                  <el-button type="primary" @click="routeTo('/project/'+field.pk)">
                    <p>赛事详情</p>
                    </el-button>
                  <!--</router-link>-->
                </div>
              </div>
              <div style="padding: 14px">
                <p> 当前报名人数 : {{ field.fields.project_hot }} </p>
                <p> 报名人数限制 : {{ field.fields.max_reg }} </p>
                <p> 比赛时间 : {{ field.fields.match_data_time | formatDate }} </p>
                <p> 比赛地点 : {{ field.fields.match_venue }} </p>
              </div>
            </div>
          </el-card>
        </el-col>
        <registerProject @dialogStatus="dialogStatus" @finish="showgroup" :dialogFormVisible="dialogVisible" :pid="project_pk" :uid="user_pk" :group="group"></registerProject>
        <registerGroup @finishGroup="hidegroup" :groupDialogFormVisible="groupVisible" :pid="project_pk" :uid="user_pk"></registerGroup>
      </el-row>
    </div>
    <br/>
    <tableList @showLogin="showLogin"></tableList>

    <br/>
    <mfooter></mfooter>
  </div>
</template>


<script>
  import auth from '../auth'
  import mheader from './header.vue'
  import mfooter from '../components/mfooter'
  import registerGroup from './CompetitionInfo/register_group.vue'
  import registerProject from './CompetitionInfo/register_project.vue'
  import tableList from './TableList.vue'

  export default {
    data () {
      return {
        carousel_img: [{
          fields: [{
            carousel_image: '',
            carousel_mark: ''
          }],
          pk: ''
        }],
        hot_project_card: [{
          fields: [{
            project_name: '',
            project_hot: '',
            max_reg: '',
            match_venue: '',
            match_data_time: ''
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
        }],
        dialogVisible: false,
        groupVisible: false,
        user_pk: '',
        project_pk: '',
        group: false
      }
    },
    created: function () {
      this.carousel_request()
      this.project_list_display()
      this.project_card_display()
      if (this.$route.params.uid && localStorage.getItem('user_id') !== this.$route.params.uid) {
        this.$router.back()
      }
      this.user_pk = this.$route.params.uid
    },
    methods: {
      getImage (index) {
        var images = require.context('../assets', false, /\.jpg$/)
        return images('./' + index)
      },
      logout () {
        auth.logout()
      },
      handleClose (done) {
        done()
      },
      routeTo (pagename) {      // two status: login in or not
        var uid = this.$route.params.uid
        if (uid) {
          this.$router.push('/' + uid + pagename)
        } else {
          this.$router.push(pagename)
        }
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
      carousel_request () {
        this.$http.get('http://127.0.0.1:8000/api/carousel_request').then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log('hello')
          console.log(res)
          if (res.error_num === 0) {
            this.carousel_img = res['list']
          } else {
            this.$message.error('获取项目列表失败"')
            console.log(res['msg'])
          }
        })
      },
      project_list_display () {
        this.$http.get('http://127.0.0.1:8000/api/project_list_display').then((response) => {
          var res = JSON.parse(response.bodyText)
//          console.log(res)
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
//          console.log(res)
          if (res.error_num === 0) {
            this.hot_project_card = res['list']
          } else {
            this.$message.error('获取项目列表失败"')
            console.log(res['msg'])
          }
        })
      },
      oneclick (pk) {
        if (!this.$route.params.uid) {
          this.showLogin()
          return
        }
        this.$http.get('http://127.0.0.1:8000/api/project_info_request/' + pk).then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            if (res.list[0].fields.group_project === true) {
              this.group = true
            }
          } else {
            this.$message.error('获取项目列表失败"')
            console.log(res['msg'])
          }
        })
        this.project_pk = pk.toString()  // has to be a string
        this.dialogVisible = true
      },
      showLogin () {
        this.$refs['header'].showMessage = true
        this.$refs['header'].dialogVisible = true
      },
      dialogStatus (val) {
        this.dialogVisible = val
      },
      showgroup () {
        this.groupVisible = true
        this.dialogVisible = false
      },
      hidegroup () {
        this.groupVisible = false
      }
    },
    components: {
      'mheader': mheader,
      'mfooter': mfooter,
      'tableList': tableList,
      'registerGroup': registerGroup,
      'registerProject': registerProject
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
    background-color: white;
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
    margin-right: 30px;
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

<template>
  <div id="CompetitionInfo">
    <div id="compinfo">
      <h1 align="left">项目：{{pageInfo.project_name}}</h1>
      <div class="basic" align="left">
        <h2 id="basicTitle">报名资料</h2>
        <el-row class="block">
          <el-col :span="12"><div class="title">比赛时间</div></el-col>
          <el-col :span="12">
            <div class="detail">
              {{pageInfo.match_data_time | formatDate }}
            </div></el-col>
        </el-row>
        <el-row class="block">
          <el-col :span="12"><div class="title">报名时间</div></el-col>
          <el-col :span="12">
            <div class="detail">
              {{pageInfo.pub_date | formatDate }} -
              {{pageInfo.ddl_date | formatDate }}
            </div></el-col>
        </el-row>
        <el-row class="block">
          <el-col :span="12"><div class="title">报名人数限制</div></el-col>
          <el-col :span="12">
            <div class="detail">
              {{pageInfo.max_reg}}
            </div></el-col>
        </el-row>
        <el-row class="block">
          <el-col :span="12"><div class="title">紧急联系人姓名</div></el-col>
          <el-col :span="12">
            <div class="detail">
              {{pageInfo.contact_name}}
            </div></el-col>
        </el-row>
        <el-row id="last" class="block">
          <el-col :span="12"><div class="title">紧急联系人电话</div></el-col>
          <el-col :span="12">
            <div class="detail">
              {{pageInfo.contact_tel}}
            </div></el-col>
        </el-row>
      </div>
      <div id="mid">
        <div class="status">
          <h2 id="statusTitle">报名状态</h2>
          <div class="bar">
            <h3>{{pageInfo.project_hot}}人已报名</h3>
            <el-progress :show-text="true" :text-inside="true" :stroke-width="18" :percentage="parseInt(attendPercent*100)"></el-progress>
          </div>
          <el-tag class="tag" v-if="rdate==='报名已结束'" type="danger">{{rdate}}</el-tag>
          <el-tag class="tag" v-else type="success">{{rdate}}</el-tag>
          <el-tag class="tag" v-if="cdate==='比赛已结束'" type="danger" size="mini">{{cdate}}</el-tag>
          <el-tag class="tag" v-else type="success">{{cdate}}</el-tag>
        </div>
        <el-button v-if="rdate==='报名已结束'" @click="$message({message: '報名已結束', type: 'warning'})" type="info" plain>報名截止</el-button>
        <el-button v-else-if="registered===true" @click="$message({message: '您已报名', type: 'warning'})" type="info" plain>已报名</el-button>
        <el-button v-else-if="attendPercent===1" @click="$message({message: '已额满', type: 'warning'})" type="info" plain>已额满</el-button>
        <el-button v-else @click="$route.params.uid!= null?dialogVisible = true:$emit('showLogin')" type="primary">立即报名</el-button>
      </div>
      <div id="qr">
          <h3>手机扫码报名</h3>
          <img src="../../assets/qr.png" />
          <div id="mobileInfo">登陆微信小程序用手机报名</div>
      </div>
    </div>
    <registerProject @dialogStatus="dialogStatus" @finish="showgroup" @error="dontshow" :dialogFormVisible="dialogVisible" :pid="project_pk" :uid="user_pk" :group="group"></registerProject>
    <registerGroup @finishGroup="hidegroup" :groupDialogFormVisible="groupVisible" :pid="project_pk" :uid="user_pk"></registerGroup>
    <div id="detail">
      <h2 align="left">详细介绍</h2>
      <div id="detailInfo">
        {{pageInfo.project_text}}
      </div>
    </div>
  </div>
</template>

<script>
import mheader from '../header.vue'
import registerGroup from './register_group.vue'
import registerProject from './register_project.vue'
export default {
  components: {
    'mheader': mheader,
    'registerGroup': registerGroup,
    'registerProject': registerProject
  },
  data () {
    return {
      pageInfo: {
        project_name: '',
        competitionTime: '',
        pub_date: '',
        ddl_date: '',
        max_reg: '',
        contact_name: '',
        contact_tel: '',
        project_hot: '',
        date: '1',
        project_text: '',
        match_data_time: ''
      },
      dialogVisible: false,
      groupVisible: false,
      project_pk: '',
      user_pk: '',
      group: false,
      registered: false
    }
  },
  computed: {
    attendPercent: function () {
      return parseFloat(this.pageInfo.project_hot) / parseFloat(this.pageInfo.max_reg)
    },
    rdate: function () {
      var today = new Date()
      var rday = new Date(this.pageInfo.ddl_date)
      var day = Math.floor((rday - today) / 1000 / 3600 / 24)
      if (day < 0) {
        return '报名已结束'
      } else {
        return '报名剩' + day + '天'
      }
    },
    cdate: function () {
      var today = new Date()
      var rday = new Date(this.pageInfo.match_data_time)
      var day = Math.floor((rday - today) / 1000 / 3600 / 24)
      if (day < 0) {
        return '比赛已结束'
      } else {
        return '比赛剩' + day + '天'
      }
    }
  },
  created: function () {
    this.project_info_request(this.$route.params.pid)
    this.user_pk = this.$route.params.uid
    this.user_register_status(this.$route.params.pid)
  },
  methods: {
    project_info_request (pk) {
      this.$http.get('http://111.230.226.45:8888/api/project_info_request/' + pk).then((response) => {
        var res = JSON.parse(response.bodyText)
        if (res.error_num === 0) {
          this.pageInfo = res.list[0].fields
          this.project_pk = res.list[0].pk
          if (res.list[0].fields.group_project === true) {
            this.group = true
          }
        } else {
          this.$message.error('获取项目列表失败"')
          console.log(res['msg'])
        }
      })
    },
    user_register_status (pk) {
      this.$http.get('http://111.230.226.45:8888/api/project_register_relationship_request/' + this.user_pk).then((response) => {
        var res = JSON.parse(response.bodyText)
        if (this.group === false) {
          for (var i = 0; i < res.list.length; i++) {
            if (res.list[i].fields.project === this.project_pk) {
              this.registered = true
              break
            }
          }
        } else {
          for (i = 0; i < res.group_list.length; i++) {
            if (res.group_list[i].fields.project === this.project_pk) {
              this.registered = true
              break
            }
          }
        }
      })
    },
    dialogStatus (val) {
      this.dialogVisible = false
    },
    showgroup () {
      this.groupVisible = true
      this.dialogVisible = false
    },
    dontshow () {
      this.dialogVisible = false
    },
    hidegroup () {
      this.groupVisible = false
    }
  }
}
</script>

<style scoped>
  #login {
    float: right;
  }
  #compinfo{
    margin: 20px;
    text-align: left;
    border-bottom: solid 1px lightgrey;
    padding-bottom: 40%;
  }
  .basic{
    padding: 3%;
    float: left;
    width: 35%;
    margin-top: 20px;
    border-radius: 4px;
    border: 1px solid #e6ebf5;
    background-color: rgb(238,241,246);
    box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
  }
  #basicTitle {
    margin-top: -5%;
  }
  .title {
    font-size: 17px;
    display: inline;
    color: #5A5E66;
  }
  .block {
    border-top: solid 1px lightgrey;
    padding-top:3%;
    padding-bottom: 3%;
  }
  .detail {
    display: inline;
    font-size: 17px;
  }
  #last {
    border-bottom: 0px;
  }
  #mid {
    float: left;
    width: 30%;
    margin-left: 5%;
    margin-top: 20px;
  }
  .status {
    padding: 10%;
    border-radius: 4px;
    border: 1px solid #e6ebf5;
    background-color: rgb(238,241,246);
    box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
  }
  #statusTitle {
    margin-top: -5%;
    border-bottom: solid 1px lightgrey;
    padding-bottom: 3%;
  }
  .tag {
    margin:1%;
    font-size: 15px;
    height: 40px;
    line-height: 40px;
  }
  .el-progress{
    width: 100%;
    padding-right: 50px;
    margin-top: 20px;
    margin-bottom: 20px;
  }
  .el-button--primary {
    width: 100%;
    line-height: 1.2;
    border-radius: 20px;
    margin-top: 30px;
  }
  .el-button--info {
    width: 100%;
    line-height: 1.2;
    border-radius: 20px;
    margin-top: 30px;
  }
  .el-button, .el-textarea__inner {
    font-size: 35px;
    border: -20px;
  }
  #qr{
    float: left;
    width: 20%;
    margin-left: 5%;
    margin-top: 20px;
    border: 2px solid silver;
    border-radius: 10px;
    padding: 20px;
    background-color: white;
  }
  #qr h3{
    text-align: center;
  }
  #qr img {
    margin-left: 0%;
    width: 100%;
    height: auto;
  }
  #mobileInfo {
    text-align: center;
    font-size: 10px;
  }
  #detail{
    width: 67%;
    clear: left;
    margin-left: 2%;
    padding: 3%;
    border-radius: 4px;
    border: 1px solid #e6ebf5;
    background-color: rgb(238,241,246);
    box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
  }
  #detail h2 {
    margin-top: -2%;
  }
  #detailInfo {
    margin-left: 1%;
  }
</style>

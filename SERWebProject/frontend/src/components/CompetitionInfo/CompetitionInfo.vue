<template>
  <div id="CompetitionInfo">
    <div id="compinfo">
      <h1 align="left">項目：{{pageInfo.project_name}}</h1>
      <div class="basic" align="left">
        <h2 id="basicTitle">報名資料</h2>
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
          <h2 id="statusTitle">報名狀態</h2>
          <div class="bar">
            <h3>{{pageInfo.project_hot}}人已報名</h3>
            <el-progress :show-text="true" :text-inside="true" :stroke-width="18" :percentage="parseInt(attendPercent*100)"></el-progress>
          </div>
          <el-tag class="tag" v-if="rdate==='报名已结束'" type="danger">{{rdate}}</el-tag>
          <el-tag class="tag" v-else type="success">{{rdate}}</el-tag>
          <el-tag class="tag" v-if="cdate==='比赛已结束'" type="danger" size="mini">{{cdate}}</el-tag>
          <el-tag class="tag" v-else type="success">{{cdate}}</el-tag>
        </div>
        <el-button id="submit" @click="$route.params.uid!= null?dialogVisible = true:$emit('showLogin')" type="primary">立即报名</el-button>
      </div>
      <div id="qr">
          <h3>手机扫码报名</h3>
          <img src="../../assets/qr.png" />
          <div id="mobileInfo">登錄微信小程序用手機報名</div>
    </div>
    </div>
    <registerProject @dialogStatus="dialogStatus" @finish="showgroup" :dialogFormVisible="dialogVisible" :pid="project_pk" :uid="user_pk" :group="group"></registerProject>
    <registerGroup @finishGroup="hidegroup" :groupDialogFormVisible="groupVisible" :pid="project_pk" :uid="user_pk"></registerGroup>
    <div id="detail">   
      <h2 align="left">详细介绍</h2>
      <div>
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
      group: false
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
  },
  methods: {
    project_info_request (pk) {
      this.$http.get('http://127.0.0.1:8000/api/project_info_request/' + pk).then((response) => {
        var res = JSON.parse(response.bodyText)
        console.log(res)
        if (res.error_num === 0) {
          this.pageInfo = res.list[0].fields
          this.pageInfo.attend = '30'
          this.project_pk = res.list[0].pk
          if (res.list[0].fields.group_project === true) {
            this.groudiv = true
          }
        } else {
          this.$message.error('获取项目列表失败"')
          console.log(res['msg'])
        }
      })
    },
    dialogStatus (val) {
      this.dialogVisible = val
    },
    showgroudiv () {
      this.groupVisible = true
      this.dialogVisible = false
    },
    hidegroudiv () {
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
    border-radius: 10px;
    background-color: #EDF2FC;
    box-shadow: 1px 1px 1px lightgray;
  }
  #basicTitle {
    margin-top: -5%;
  }
  .title {
    font-size: 17px;
    display: inline;
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
    border-radius: 10px;
    background-color: #EDF2FC;
    box-shadow: 1px 1px 1px lightgray;
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
  #qr p{
  }
  #qr img {
    margin-left: 0%;
    width: 100%;
    height: auto;
  }
  #mobileInfo {
    font-size: 10px;
  }
  #detail{
    margin-left: 5%;
    clear: left;
  }
  #detail h2{
    font-size: 25px;
  } 
</style>

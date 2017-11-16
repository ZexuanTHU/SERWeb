<template>
  <div id="CompetitionInfo">
    <div id="compinfo">
      <h1 align="left">{{pageInfo.project_name}}</h1>
      <div id="basic" >
        <p align="left">
          比赛时间:<br>
          {{pageInfo.match_data_time}}
        </p>
        <p align="left">
          报名时间: <br>
          from: {{pageInfo.pub_date}}<br>
          to: {{pageInfo.ddl_date}}
        </p>
        <p align="left">
          报名人数限制: {{pageInfo.max_reg}}
        </p>
        <p align="left">
          紧急联系人姓名: {{pageInfo.contact_name}}
        </p>
        <p align="left">
          紧急联系人电话: {{pageInfo.contact_tel}}
        </p>
      </div>
      <div class="status">
        <h3>{{pageInfo.project_hot}}人已報名</h3>
        <el-progress :show-text="false" :stroke-width="18" :percentage="parseInt(attendPercent*100)"></el-progress>
        <h3>{{rdate}}</h3>
        <h3>{{cdate}}</h3>
      </div>
      <el-button id="submit" @click="$route.params.uid!= null?dialogVisible = true:$emit('showLogin')" type="primary">报名</el-button>
      <registerProject @dialogStatus="dialogStatus" @finish="showgroup" :dialogFormVisible="dialogVisible" :pid="project_pk" :uid="user_pk" :group="group"></registerProject>
      <registerGroup @finishGroup="hidegroup" :groupDialogFormVisible="groupVisible" :pid="project_pk" :uid="user_pk"></registerGroup>
      <div id="detail">
        <hr>
        <h2 align="left">详细介绍</h2>
        <p>
          {{pageInfo.project_text}}
        </p>
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
            this.group = true
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
    showgroup () {
      this.groupVisible = true
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
  }
  #basic{
    float: left;
    width: 30%;
  }
  #detail{
    clear: left;
  }
  .status {
    width: 70%;
  }
  .status el-progress{
    padding-right: 50px;
    margin-top: 20px;
    margin-bottom: 20px;
    width: 10px;
  }
  #submit #group{
    margin-top: 20px;
    margin-bottom: 20px;
  }
</style>

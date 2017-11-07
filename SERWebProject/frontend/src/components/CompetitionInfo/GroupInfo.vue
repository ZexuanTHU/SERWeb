<template>
  <div id="GroupInfo">
    <mheader></mheader>
    <div id="compinfo">
      <h1 align="left">{{pageInfo.project_name}}</h1>
      <div id="basic" >
        <p align="left">
          比赛时间: {{pageInfo.competitionTime}}
        </p>
        <p align="left">
          报名时间: {{pageInfo.pub_date}}--{{pageInfo.ddl_date}}
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
        <el-progress :show-text="false" :stroke-width="18" :percentage="parseInt(attendPercent*100)"></el-progress>
        <h3>{{pageInfo.attend}}人報名</h3>
        <el-progress :show-text="false" :stroke-width="18" :percentage="90"></el-progress>
        <h3>剩下{{date}}天</h3>
      </div>
      <el-button id="submit" @click="dialogFormVisible = true" type="primary">立即报名</el-button>
      <registerGroup :dialogFormVisible="dialogFormVisible" :projectpk="project_pk"></registerGroup>
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
export default {
  components: {
    'mheader': mheader,
    'registerGroup': registerGroup
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
        attend: '30',
        date: '1',
        project_text: ''
      },
      dialogFormVisible: false,
      project_pk: ''
    }
  },
  computed: {
    attendPercent: function () {
      return parseFloat(this.pageInfo.attend) / parseFloat(this.pageInfo.max_reg)
    }
  },
  created: function () {
    this.project_info_request(this.$route.params.pk)
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
        } else {
          this.$message.error('获取项目列表失败"')
          console.log(res['msg'])
        }
      })
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
  .status el-progress{
    padding-right: 50px;
    margin-top: 20px;
    margin-bottom: 20px;
  }
  #submit{
    margin-top: 20px;
    margin-bottom: 20px;
  }
</style>

<template>
  <div id="more news" style="margin-left: 5%; margin-right: 6.5%">
    <h1 align="left">其他赛事</h1>
    <br/>
    <registerProject @dialogStatus="dialogStatus" @finish="showgroup" :dialogFormVisible="dialogVisible" :pid="project_pk" :uid="user_pk" :group="group"></registerProject>
    <registerGroup @finishGroup="hidegroup" :groupDialogFormVisible="groupVisible" :pid="project_pk" :uid="user_pk"></registerGroup>
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
        <template scope="scope"> {{ scope.row.fields.pub_date | formatDate }}~{{ scope.row.fields.ddl_date | formatDate }} </template>
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
          <el-button @click="oneclick(scope.row.pk)" style="padding: 1px; height: 30px; margin-right: -10px">
            一键报名
          </el-button>
          <!--<router-link :to="{name: 'project', params: {uid:$route.params.uid, pid: scope.row.pk}}">-->
          <el-button type="primary" @click="routeTo('/project/'+scope.row.pk)" style="padding: 1px; height: 30px;">
            赛事详情
          </el-button>
          <!--</router-link>-->
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  import registerGroup from './CompetitionInfo/register_group.vue'
  import registerProject from './CompetitionInfo/register_project.vue'

  export default {
    components: {
      'registerGroup': registerGroup,
      'registerProject': registerProject
    },
    data () {
      return {
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
      this.project_list_display()
      this.user_pk = this.$route.params.uid
    },
    methods: {
      routeTo (pagename) {      // two status: login in or not
        var uid = this.$route.params.uid
        if (uid) {
          this.$router.push('/' + uid + pagename)
        } else {
          this.$router.push(pagename)
        }
      },
      project_list_display () {
        this.$http.get('http://111.230.226.45:8888/api/project_list_display').then((response) => {
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
      oneclick (pk) {
        if (!this.$route.params.uid) {
          this.$emit('showLogin')
          return
        }
        this.$http.get('http://111.230.226.45:8888/api/project_info_request/' + pk).then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            if (res.list[0].fields.group_project === true) {
              this.group = true
            } else {
              this.group = false
            }
          } else {
            this.$message.error('获取项目列表失败"')
            console.log(res['msg'])
          }
        })
        this.project_pk = pk.toString()
        this.dialogVisible = true
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

<style>

</style>

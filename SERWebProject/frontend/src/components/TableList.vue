<template>
  <div id="more news" style="margin-left: 5%; margin-right: 6.5%">
    <h1 align="left">其他赛事</h1>
    <br/>
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
          <el-button size="mini">
            <p>一键报名</p>
          </el-button>
          <router-link :to="{name: 'project', params: {uid:$route.params.uid, pid: scope.row.pk}}">
            <el-button type="primary" size="mini">
              <p style="color: white">赛事详情</p>
            </el-button>
          </router-link>

        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  export default {
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
        }]
      }
    },
    created: function () {
      this.project_list_display()
    },
    methods: {
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
      }
    }
  }
</script>

<style>

</style>

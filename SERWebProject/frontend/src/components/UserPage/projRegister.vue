<template>
  <div id="more news">
    <h1 align="center">比赛列表</h1>
    <el-table
      :data="latest_project_list"
      height="200"
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
          <el-button  type="text" size="small">
            <router-link to="CompetitionInfo">报名</router-link>
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>

</template>

<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");

  a {
    text-decoration: none;
  }
</style>

<script>
  export default {
    data () {
      return {
        latest_project_list: [{
          fields: [{
            project_name: '',
            project_text: '',
            ddl_date: '',
            pub_date: '',
            max_reg: '',
            contact_name: '',
            contact_tel: ''
          }],
          pk: ''
        }]
      }
    }
  }
</script>

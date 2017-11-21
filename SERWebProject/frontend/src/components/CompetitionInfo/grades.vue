<template>
  <el-table
    :data="tableData"
    style="width: 100%"
    :default-sort = "{prop: 'rank', order: 'ascending'}"
    >
    <el-table-column
      prop="fields.rank"
      label="名次"
      width="180">
    </el-table-column>
    <el-table-column v-if="group === false"
      prop="fields.register_name"
      label="姓名"
      width="180">
    </el-table-column>
    <el-table-column v-else
      prop="fields.group_name"
      label="隊名"
      width="180">
    </el-table-column>
    <el-table-column v-if="group === false"
      prop="fields.registered_project_name"
      label="項目">
    </el-table-column>
    <el-table-column v-else
      prop="fields.team_creator_name"
      label="隊長">
    </el-table-column>
    <el-table-column v-if="group === false"
      prop="fields.student_id"
      label="學號">
    </el-table-column>
    <el-table-column v-else
      prop="fields.teammate_num"
      label="隊員人數">
    </el-table-column>
    <el-table-column
      prop="fields.grade"
      label="成績">
    </el-table-column>
  </el-table>
</template>

<script>
  export default {
    data () {
      return {
        tableData: [{
          fields: {
            user: '',
            grade: '',
            regitster_name: '',
            registered_project_name: '',
            other: '--',
            student_id: '',
            if_group_project: false
          }
        }],
        group: false
      }
    },
    created: function () {
      this.getGrade(this.$route.params.pid)
    },
    methods: {
      getGrade (pid) {
        this.$http.get('http://111.230.226.45:8888/api/project_grade_request/' + pid).then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.tableData = res['list']
            if (this.tableData[0].fields.if_group_project === true) {
              this.group = true
            }
            console.log(this.tableData)
          } else {
            this.$message.error('获取项目列表失败"')
            console.log(res['msg'])
          }
        })
      }
    }
  }
</script>

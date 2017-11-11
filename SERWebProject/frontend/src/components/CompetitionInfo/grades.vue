<template>
  <el-table
    :data="tableData"
    style="width: 100%"
    :default-sort = "{prop: 'grade', order: 'ascending'}"
    >
    <el-table-column
      prop="fields.grade"
      label="名次"
      width="180">
    </el-table-column>
    <el-table-column
      prop="fields.register_name"
      label="姓名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="fields.registered_project_name"
      label="項目">
    </el-table-column>
    <el-table-column
      prop="fields.student_id"
      label="学号">
    </el-table-column>
    <el-table-column
      prop="fields.other"
      label="備註">
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
            student_id: ''
          }
        }]
      }
    },
    created: function () {
      this.getGrade(this.$route.params.pid)
    },
    methods: {
      getGrade (pid) {
        this.$http.get('http://localhost:8000/api/project_grade_request/' + pid).then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.tableData = res['list']
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
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
      <el-button id="submit" @click="dialogFormVisible = true, user_info_request('skyrealmz')" type="primary">立即报名</el-button>
      <el-dialog title="團隊報名" :visible.sync="dialogFormVisible">
        <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="100px" class="demo-dynamic">
          <el-form-item
            prop="name"
            label="隊長姓名"
            :rules="[
              { required: true, message: '请输入隊長姓名', trigger: 'blur' },
              { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
            ]"
          >
            <el-input v-model="dynamicValidateForm.name"></el-input>
          </el-form-item>
          <el-form-item
            v-for="(teamate, index) in dynamicValidateForm.teamates"
            :label="'队员' + index"
            :key="teamate.key"
            :prop="'teamates.' + index + '.value'"
            :rules="[
            {required: true, message: '队员不能为空', trigger: 'blur'},
            { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
            ]"
          >
            <el-input v-model="teamate.value"></el-input>
            <el-button @click.prevent="removeteamate(teamate)">删除</el-button>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('dynamicValidateForm')">提交</el-button>
            <el-button @click="addteamate">新增队友</el-button>
            <el-button @click="resetForm('dynamicValidateForm')">重置</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>
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
export default {
  components: {
    'mheader': mheader
  },
  data () {
    return {
      dynamicValidateForm: {
        teamates: [{
          value: ''
        }],
        name: ''
      },
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
      ruleForm: {
        faculty: '',
        name: '',
        gender: '',
        id_card: '',
        student_id: '',
        birth_date: '',
        clothes_size: '',
        cellphone_num: ''
      },
      formLabelWidth: '120px'
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
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    removeteamate (item) {
      var index = this.dynamicValidateForm.teamates.indexOf(item)
      if (index !== -1) {
        this.dynamicValidateForm.teamates.splice(index, 1)
      }
    },
    addteamate () {
      this.dynamicValidateForm.teamates.push({
        value: '',
        key: Date.now()
      })
    },
    project_info_request (pk) {
      this.$http.get('http://127.0.0.1:8000/api/project_info_request/' + pk).then((response) => {
        var res = JSON.parse(response.bodyText)
        console.log(res)
        if (res.error_num === 0) {
          this.pageInfo = res.list[0].fields
          this.pageInfo.attend = '30'
        } else {
          this.$message.error('获取项目列表失败"')
          console.log(res['msg'])
        }
      })
    },
    user_info_request (username) {
      this.$http.get('http://127.0.0.1:8000/api/user_info_request?username=' + username).then((response) => {
        var res = JSON.parse(response.bodyText)
        console.log(res)
        if (res.error_num === 0) {
          this.dynamicValidateForm.name = res.list[0].fields.name
          this.ruleForm.birth_date = ''
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

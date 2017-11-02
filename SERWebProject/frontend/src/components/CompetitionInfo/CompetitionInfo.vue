<template>
  <div id="CompetitionInfo">
    <div id="nav">
      <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1"><router-link to="./">首页</router-link></el-menu-item>
        <el-submenu index="2">
          <template slot="title">项目列表</template>
          <el-menu-item index="2-1">项目报名</el-menu-item>
          <el-menu-item index="2-2">比赛日程</el-menu-item>
        </el-submenu>
        <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">历史沿革</a></el-menu-item>
        <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">院系荣誉</a></el-menu-item>
        <el-menu-item index="5"><a href="https://www.ele.me" target="_blank">突出个人</a></el-menu-item>
        <el-menu-item index="6"><a href="https://www.ele.me" target="_blank">加入院队</a></el-menu-item>
        <el-menu-item id="login" index="7">
          <router-link to="Login">用户信息</router-link>
        </el-menu-item>
      </el-menu>
    </div>
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
      <el-dialog title="报名资料确认" :visible.sync="dialogFormVisible">
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item label="院系" prop="faculty">
            <el-select v-model="ruleForm.faculty" placeholder="选择院系">
              <el-option label="计算机" value="CS"></el-option>
              <el-option label="自动化" value="AUTO"></el-option>
              <el-option label="电子" value="EE"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="名字" prop="name">
            <el-input v-model="ruleForm.name"></el-input>
          </el-form-item>
          <el-form-item label="性别" prop="gender">
            <el-select v-model="ruleForm.gender" placeholder="选择性别">
              <el-option label="男" value="M"></el-option>
              <el-option label="女" value="F"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="证件号码" prop="id_card">
            <el-input v-model="ruleForm.id_card"></el-input>
          </el-form-item>
          <el-form-item label="学号" prop="student_id">
            <el-input v-model="ruleForm.student_id"></el-input>
          </el-form-item>
          <el-form-item prop="birth_date">
            <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.birth_date" style="width: 100%;"></el-date-picker>
          </el-form-item>
          <el-form-item label="服装号码" prop="clothes_size">
            <el-select v-model="ruleForm.clothes_size" placeholder="选择号码">
              <el-option label="S" value="S"></el-option>
              <el-option label="M" value="M"></el-option>
              <el-option label="L" value="L"></el-option>
              <el-option label="XL" value="XL"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="移动电话" prop="cellphone_num">
            <el-input v-model="ruleForm.cellphone_num"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">报名</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
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
export default {
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
      user_pk: '',
      project_pk: '',
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
      rules: {
        faculty: [
          { required: true, message: '请选择院系', trigger: 'change' }
        ],
        name: [
          { required: true, message: '请输入名字', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        gender: [
          { required: true, message: '请选性别', trigger: 'change' }
        ],
        id_card: [
          { required: true, message: '请输入身份证号码', trigger: 'blur' },
          { min: 0, max: 20, message: '长度在 x 到 x 个字符', trigger: 'blur' }
        ],
        student_id: [
          { required: true, message: '请输入学号', trigger: 'blur' },
          { legth: 10, message: '长度10个字符', trigger: 'blur' }
        ],
        birth_date: [
          { type: 'date', message: '请选择生日', trigger: 'change' }
        ],
        clothes_size: [
          { required: true, message: '请选择衣服号码', trigger: 'change' }
        ],
        cellphone_num: [
          { required: true, message: '请输入学号', trigger: 'blur' },
          { min: 12, max: 12, message: '长度12个字符', trigger: 'blur' }
        ]
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
    },
    user_info_request (username) {
      this.$http.get('http://127.0.0.1:8000/api/user_info_request?username=' + username).then((response) => {
        var res = JSON.parse(response.bodyText)
        console.log(res)
        if (res.error_num === 0) {
          this.ruleForm = res.list[0].fields
          this.ruleForm.birth_date = ''
          this.user_pk = res.list[0].pk
        } else {
          this.$message.error('获取项目列表失败"')
          console.log(res['msg'])
        }
      })
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$http.get('http://127.0.0.1:8000/api/project_register/' + this.user_pk + '/' + this.project_pk)
          this.dialogFormVisible = false
          alert('報名成功')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style scoped>

  a {
    text-decoration: none;
  }

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

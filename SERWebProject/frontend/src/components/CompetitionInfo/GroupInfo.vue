<template>
  <div id="GroupInfo">
    <div id="nav">
      <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1">首页</el-menu-item>
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
      <h1 align="left">{{name}}</h1>
      <div id="basic">
        <p align="left">
          比赛时间: {{competitionTime}}
        </p>
        <p align="left">
          报名时间: {{registerTime}}
        </p>
        <p align="left">
          紧急联系人姓名：{{contanct}}
        </p>
        <p align="left">
          紧急联系人电话: {{contanctphone}}
        </p>
        <p align="left">
          竞赛类别: {{catagory}}
        </p>
        <p align="left">
          主办单位: {{host}}
        </p>
        <p>
          参赛资格: {{qualification}}
        </p>
      </div>
      <div class="status">
        <el-progress :show-text="false" :stroke-width="18" :percentage="30"></el-progress>
        <h3>{{attend}}人報名</h3>
        <el-progress :show-text="false" :stroke-width="18" :percentage="90"></el-progress>
        <h3>剩下{{date}}天</h3>
      </div>
      <el-button id="submit" @click="dialogFormVisible = true, user_info_request('skyrealmz')" type="primary">立即报名</el-button>
      <el-dialog title="隊長资料填写" :visible.sync="dialogFormVisible">
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
          {{detail}}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      name: '2017年清华大学校园马拉松',
      competitionTime: '2017／03／06 14：00',
      registerTime: '2017-03-02  --  2017-03-05',
      contact: '郭志芃',
      contactphone: '18813040000',
      catagory: '團體',
      host: '计算机系',
      qualification: '计算机系同学',
      attend: '30',
      date: '1',
      detail: '足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛',
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
      rules: {
        faculty: [
          { required: true, message: '请选择院系' }
        ],
        name: [
          { required: true, message: '请输入名字', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        gender: [
          { required: true, message: '请选性别' }
        ],
        id_card: [
          { required: true, message: '请输入身份证号码', trigger: 'blur' },
          { min: 0, max: 20, message: '长度在 x 到 x 个字符', trigger: 'blur' }
        ],
        student_id: [
          { required: true, message: '请输入学号', trigger: 'blur' },
          { min: 10, max: 10, message: '长度10个字符', trigger: 'blur' }
        ],
        birth_date: [
          { required: true, message: '请选择生日' }
        ],
        clothes_size: [
          { required: true, message: '请选择衣服号码' }
        ],
        cellphone_num: [
          { required: true, message: '请输入学号', trigger: 'blur' },
          { min: 12, max: 12, message: '长度12个字符', trigger: 'blur' }
        ]
      },
      formLabelWidth: '120px'
    }
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
    user_info_request (username) {
      this.$http.get('http://127.0.0.1:8000/api/user_info_request?username=' + username).then((response) => {
        var res = JSON.parse(response.bodyText)
        console.log(res)
        if (res.error_num === 0) {
          this.ruleForm = res.list[0].fields
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

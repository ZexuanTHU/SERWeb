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
      <el-button id="submit" @click="dialogFormVisible = true" type="primary">立即报名</el-button>
      <el-dialog title="隊長资料填写" :visible.sync="dialogFormVisible">
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item label="院系" prop="department">
            <el-select v-model="ruleForm.department" placeholder="选择院系">
              <el-option label="计算机" value="cs"></el-option>
              <el-option label="自动化" value="auto"></el-option>
              <el-option label="电子" value="ee"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="名字" prop="name">
            <el-input v-model="ruleForm.name"></el-input>
          </el-form-item>
          <el-form-item label="性别" prop="gender">
            <el-select v-model="ruleForm.gender" placeholder="选择性别">
              <el-option label="男" value="male"></el-option>
              <el-option label="女" value="female"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="证件号码" prop="idNumber">
            <el-input v-model="ruleForm.idNumber"></el-input>
          </el-form-item>
          <el-form-item label="学号" prop="studentId">
            <el-input v-model="ruleForm.studentId"></el-input>
          </el-form-item>
          <el-form-item prop="birth">
            <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.birth" style="width: 100%;"></el-date-picker>
          </el-form-item>
          <el-form-item label="服装号码" prop="clothSize">
            <el-select v-model="ruleForm.clothSize" placeholder="选择号码">
              <el-option label="S" value="s"></el-option>
              <el-option label="M" value="m"></el-option>
              <el-option label="L" value="l"></el-option>
              <el-option label="XL" value="xl"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="移动电话" prop="phone">
            <el-input v-model="ruleForm.phone"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
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
        department: '',
        name: '',
        gender: '',
        idNumber: '',
        studentId: '',
        birth: '',
        clothSize: '',
        phone: ''
      },
      rules: {
        department: [
          { required: true, message: '请选择院系', trigger: 'change' }
        ],
        name: [
          { required: true, message: '请输入名字', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        gender: [
          { required: true, message: '请选性别', trigger: 'change' }
        ],
        idNumber: [
          { required: true, message: '请输入身份证号码', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        studentId: [
          { required: true, message: '请输入学号', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        birth: [
          { required: true, message: '请选择生日', trigger: 'change' }
        ],
        clothSize: [
          { required: true, message: '请选择衣服号码', trigger: 'change' }
        ],
        phone: [
          { required: true, message: '请输入学号', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
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

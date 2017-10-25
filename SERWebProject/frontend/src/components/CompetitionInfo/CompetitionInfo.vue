<template>
  <div id="CompetitionInfo">
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
          时间: {{time}}
        </p>
        <p align="left">
          地点: {{location}}
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
      <el-dialog title="报名资料填写" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="名字" :label-width="formLabelWidth">
            <el-input v-model="form.name" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="项目" :label-width="formLabelWidth">
            <el-select v-model="form.region" placeholder="请选择报名项目">
              <el-option label="半程" value="half"></el-option>
              <el-option label="全程" value="whole"></el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
        </div>
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
      name: '足球錦標賽',
      time: '12/32 14:30',
      location: '操场',
      catagory: '⚽️',
      host: '计算机系',
      qualification: '计算机系同学',
      attend: '30',
      date: '1',
      detail: '足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛',
      dialogFormVisible: false,
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      formLabelWidth: '120px'
    }
  }
}
</script>

<style>
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

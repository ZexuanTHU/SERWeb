<template>
  <div>
    <mheader></mheader>
    <div class="w3-content" style="max-width:2000px;margin-top:6px">
      <div class="w3-container" style="width: 100%;min-height: 650px">
        <div class="w3-left" style="width: 200px;height: 100% ">
          <el-col :span="8">
            <h5></h5>
            <el-menu id="leftnav" default-active="4" class="el-menu-vertical-demo" @select="openPanel">

              <el-menu-item index="0">2013</el-menu-item>
              <el-menu-item index="1"></el-menu-item>
              <el-menu-item index="2"></el-menu-item>
              <el-menu-item index="3"></el-menu-item>
              <el-menu-item index="4"></el-menu-item>
            </el-menu>
          </el-col>
        </div>
        <div class="panel_content" style="margin-left:200px;display: block;padding-top:30px">
          <div class="w3-container panel"
               :style="{display:openedPanel==='0'?'inline-block':'none'}">
            <el-row>
              <el-col :span="8" v-for="(o, index) in 2" :key="o" :offset="index > 0 ? 2 : 0">
                <el-card :body-style="{ padding: '0px' }" style="margin-top: 4%">
                  <img @click="dialogVisible = true" src="../assets/halloffame.jpg" class="image">
                  <div style="padding: 14px;">
                    <span>李晨曦</span>
                  </div>
                </el-card>
              </el-col>
            </el-row>
            <el-dialog
              title="李晨曦"
              :visible.sync="dialogVisible"
              size="large">
              <div>
                <el-tabs v-model="activeName" @tab-click="handleClick">
                  <el-tab-pane label="User" name="first">
                    <ul v-for="item in items">
                      <li> 性别 : {{ item.gender }} </li>
                      <li> 级数 : {{ item.grade }} </li>
                      <li> 班级 : {{ item.class }} </li>
                      <li> 擅长项目 : {{ item.expertise }} </li>
                    </ul>
                  </el-tab-pane>
                  <el-tab-pane label="Config" name="second">Config</el-tab-pane>
                  <el-tab-pane label="Role" name="third">Role</el-tab-pane>
                  <el-tab-pane label="Task" name="fourth">Task</el-tab-pane>
                </el-tabs>
              </div>
            </el-dialog>
          </div>
        </div>
        </div>
    </div>
      <mfooter></mfooter>
  </div>
</template>

<script>
  import mheader from '@/components/header'
  import mfooter from '../components/mfooter'

  export default {
    data () {
      return {
        openedPanel: '0',
        dialogVisible: false,
        activeName: 'first',
        items: [{
          name: '李晨曦',
          gender: '男',
          grade: '2013级',
          class: 'xx 班',
          expertise: '中长跑'
        }]
      }
    },
    methods: {
      openPanel: function (index) {
        this.openedPanel = index
      },
      handleClick (tab, event) {
        console.log(tab, event)
      }
    },
    components: {
      'mheader': mheader,
      'mfooter': mfooter
    }
  }
</script>

<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");
  @import "../css/w3.css";
  @import "../css/user.css";

  a {
    text-decoration: none;
  }

  #leftnav {
    margin-top: 40px;
    width: 200px;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }
</style>

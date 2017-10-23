<template>
  <div>
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

    <div id="carousel">
      <el-carousel :interval="5000" arrow="always">
        <el-carousel-item v-for="item in 4" :key="item">
          <h3>test</h3>
        </el-carousel-item>
      </el-carousel>
    </div>

    <div id="hot news">
      <h1 align="left">热门赛事</h1>
      <a href="" target="_blank" id="more">查看更多 ></a>
      <el-row>
        <el-col :span="8" v-for="(o, index) in 2" :key="o" :offset="index > 0 ? 2 : 0">
          <el-card :body-style="{ padding: '0px' }">
            <img src="https://www.kingsford.com/wp-content/uploads/2014/11/kfd-howtohamburger-Burgers_5_0391-1024x621.jpg" class="image">
            <div style="padding: 14px;">
              <span>Yummy hamburger</span>
              <div class="bottom clearfix">
                <time class="time">{{ currentDate }}</time>
                <el-button type="text" class="button"><router-link to="CompetitionInfo">Operating button</router-link></el-button>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>

    <div id="more news">
      <h1 align="left">其他赛事</h1>
      <el-table
        :data="tableData"
        border
        style="width: 100%">
        <el-table-column
          prop="event"
          label="赛事名称"
          sortable
          align="center">
        </el-table-column>
        <el-table-column
          prop="time"
          label="时间"
          align="center">
        </el-table-column>
        <el-table-column
          prop="host"
          label="主办单位"
          align="center">
        </el-table-column>
        <el-table-column
          prop="type"
          label="种类"
          align="center">
        </el-table-column>
        <el-table-column
          prop="tag"
          label="Tag"
          align="center"
          :filters="[{ text: '已报名', value: '已报名' }, { text: '还没报名', value: '立即报名' }]"
          :filter-method="filterTag"
          filter-placement="bottom-end">
          <template scope="scope">
            <el-tag
              :type="scope.row.tag === 'Home' ? 'primary' : 'success'"
              close-transition>{{scope.row.tag}}</el-tag>
          </template>
        </el-table-column>
      </el-table>
    </div>

  </div>
</template>


<script>
  export default {
    data () {
      return {
        activeIndex: '1',
        activeIndex2: '1',
        activeName: 'first',
        currentDate: new Date(),
        tableData: [{
          event: 'event',
          time: '111',
          host: '学生会',
          type: '篮球',
          tag: '立即报名'
        }, {
          event: 'event',
          time: '111',
          host: '学生会',
          type: '篮球',
          tag: '立即报名'
        }, {
          event: 'event',
          time: '111',
          host: '学生会',
          type: '篮球',
          tag: '立即报名'
        }, {
          event: 'event',
          time: '111',
          host: '学生会',
          type: '篮球',
          tag: '立即报名'
        }]
      }
    },
    methods: {
      handleSelect (key, keyPath) {
        console.log(key, keyPath)
      },
      handleClick (tab, event) {
        console.log(tab, event)
      },
      formatter (row, column) {
        return row.address
      },
      filterTag (value, row) {
        return row.tag === value
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");

  a {
    text-decoration: none;
  }

  #login {
    float: right;
  }

  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  #hot {
    margin-top: 10px;
    margin-bottom: 20px;
  }

  #more {
    float: right;
    font-size: 12px;
    font-family: sans-serif;
    color: #999999;
    margin-right: 22px;
  }

  .time {
    font-size: 13px;
    color: #999;
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


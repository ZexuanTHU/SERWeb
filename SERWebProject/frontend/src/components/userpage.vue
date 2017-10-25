<template>
  <div>

    <mheader></mheader>
    <!-- Page content -->
    <div class="w3-content" style="max-width:2000px;margin-top:46px">
      <div class="w3-container" style="width: 100%;min-height: 650px">
        <div class="w3-left" style="width: 200px;height: 100% ">
          <div class="w3-card-2 w3-left leftbar"
               style="width:200px;height: 420px;margin-top: 20px;display: block;background:#eef1f6;text-align:center;">
            <div class="w3-card" style="border: solid 1px;background:#4d65fc;height: 20px">
            </div>
            <p @click="openPanle('register')" class="tablink" href="#" :class="{'pressed':(openedPanle==='register')}"
               style="margin-top:10px">比赛报名</p>
            <p v-on:click="openPanle('view_register')" class="tablink" href="#"
               :class="{'pressed':(openedPanle==='view_register')}">报名结果</p>
            <p v-on:click="openPanle('saved_event')" class="tablink" :class="{'pressed':(openedPanle==='saved_event')}">
              比赛收藏</p>
            <p v-on:click="openPanle('modify')" class="tablink" :class="{'pressed':(openedPanle==='modify')}">个人信息</p>
            <p v-on:click="openPanle('add_event')" class="tablink" :class="{'pressed':(openedPanle==='add_event')}">
              创建比赛</p>
          </div>
        </div>
        <div class="panel_content" style="margin-left:200px;display: block; ">

          <div id="register" class="w3-container panel"
               :style="{display:openedPanle==='register'?'inline-block':'none'}">
            <h1 style="font-size: large;margin: auto">regiser</h1>
          </div>
          <div id="saved_event" class="w3-container panel"
               :style="{display:openedPanle==='saved_event'?'inline-block':'none'}">
            <h1 style="font-size: large;margin: auto">saved_event</h1>
          </div>
          <div id="view_register" class="w3-container panel "
               :style="{display:openedPanle==='view_register'?'inline-block':'none'}">
            <h1 style="font-size: large;margin: auto">view_regiser</h1>
          </div>
          <div id="modify" class="w3-container panel" style="display: inline-block"
               :style="{display:openedPanle==='modify'?'inline-block':'none'}">
            <form action="" @change="saveToLocal($event.target.name,$event.target.value)">
              <p style="margin-top: 40px"><span class="input-tag">姓名:</span> <input type="text" name="modi-name" >
              </p>
              <p><span class="input-tag">电话:</span> <input type="text" name="modi-phone" ></p>
              <p><span class="input-tag">邮箱:</span> <input type="text" name="modi-email" ></p>
              <p><span class="input-tag">学号:</span> <input type="text" name="modi-stu-id" ></p>
              <p style="height: 200px"><span class="input-tag" style="vertical-align: middle">备注:</span>
                <textarea style="margin-left:10px;width: 400px;height:200px;vertical-align: middle" name="modi-extra"
                          type="text"></textarea></p>
            </form>

            <div style="width: 240px;height: 360px;text-align: center;position: absolute;right: 200px;top: 40px">
              <img class="icon" :src="imageUrl"
                   style="width:100%;margin-bottom: 5px; height: 240px;border-style: solid;border-color: #e3d4d4;  border-radius: 20%;"
                   alt="">
              <button class="w3-button mboarderbtn " style="width: 50%;margin: auto;"
                      v-on:click="fileclick()">选择头像
              </button>
              <input id="filechooser" type="file" @change="onFileChange" style="display: none;"/>
            </div>
          </div>
          <div id="add_event" class="w3-container panel"
               :style="{display:openedPanle==='add_event'?'inline-block':'none'}">
            <h1 style="border-bottom:2px solid #72beff;margin-left: 1em ">新比赛</h1>
            <form action="" @change="saveToLocal($event.target.name,$event.target.value)">
              <p><span style="width: 100px">时间:</span> <input type="date" name="add-time">
                <span style="padding-left: 20px">地点：</span><input style="left: 500px" type="text" name="add-place"></p>
            </form>

          </div>
        </div>
      </div>
      <mfooter></mfooter>
    </div>

  </div>

</template>

<script>
  import mheader from '../components/header'
  import mfooter from '../components/mfooter'

  export default {
    name: 'test',
    data () {
      return {
        imageUrl: require('../image/icon.jpg'),
        openedPanle: 'modify_info',
        applyState: JSON.stringify({ddl: 'ddl'})

      }
    },
    methods: {
      openPanle: function openPanle (option) {
        this.openedPanle = option
      },
      onFileChange (e) {
        var files = e.target.files || e.dataTransfer.files
        if (!files.length) return
        if (!/image+/.test(files[0].type)) {
          alert('请输入一张图片')
          return
        }
        var reader = new FileReader()
        reader.onload = (e) => {
          this.imageUrl = e.target.result
        }
        reader.readAsDataURL(files[0])
      },
      fileclick: function () {
        document.getElementById('filechooser').click()
        console.log(document.getElementById('filechooser'))
      },
      saveToLocal: function (key, value) {
        try {
          localStorage.setItem(key, value)
        } catch (e) {
          console.log('save to local failed')
        }
      },
      applyInfo (statechange) {
        var newmessage = ''
        for (var i = 0; i < statechange.length; i++) {
          newmessage = newmessage.concat('您在 ' + statechange[i].gametime.toDateString() + '的 ' + statechange[i].gamename + ' 比赛报名已经' + statechange[i].state + '\r')
        }
        this.$notify.info({
          title: '报名状态更新',
          offset: 300,
          message: newmessage
        })
      },
      getstate: function () {
        return localStorage.getItem('applyState')
      },
      compareState: function (news) {
        if (news === this.applyState) return null
        this.applyState = news
        return [{
          gametime: new Date(),
          gamename: 'football',
          state: '通过'
        }]
      },
      ajaxpoll () {
        var self = this
        setInterval(function () {
          console.log('start')
          var newState = self.getstate()
          var change = self.compareState(newState)
          if (change !== null) {
//            console.log(change)
            self.applyInfo(change)
          }
        }, 5000)
      }

    },
    mounted: function () {
      var input = document.getElementsByTagName('input')
//      console.log(input)
      for (var i = 0; i < input.length; i++) {
        console.log(input[i])
        input[i].value = localStorage.getItem(input[i].name) || ''
      }
      var textarea = document.getElementsByTagName('textarea')
      for (i = 0; i < textarea.length; i++) {
        textarea[i].value = localStorage.getItem(textarea[i].name) || ''
      }
      this.ajaxpoll()
    },
    components: {
      'mheader': mheader,
      'mfooter': mfooter
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");
  @import "../css/w3.css";
  @import "../css/user.css";

  a {
    text-decoration: none;
  }

</style>

<template>
  <el-form :model="infoForm" :rules="rules" ref="ruleForm" label-width="80px" :inline="inline">
    <el-form-item label="学位" prop="degree">
      <el-select v-model="infoForm.reading_degree" placeholder="选择院系" class="mid">
        <el-option label="本科" value="BS"></el-option>
        <el-option label="硕士" value="MS"></el-option>
        <el-option label="博士" value="PhD"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="院系" prop="faculty">
      <el-select v-model="infoForm.faculty" placeholder="选择院系" class="mid">
        <el-option label="计算机" value="cs"></el-option>
        <el-option label="自动化" value="auto"></el-option>
        <el-option label="电子" value="ee"></el-option>
      </el-select>
    </el-form-item>
    <br v-if="inline">
    <el-form-item label="班级" prop="class_id">
      <el-input v-model="infoForm.class_id" class="mid"></el-input>
    </el-form-item>
    <el-form-item label="名字" prop="name">
      <el-input v-model="infoForm.name" class="mid"></el-input>
    </el-form-item>
    <br v-if="inline">
    <el-form-item label="性别" prop="gender">
      <el-select v-model="infoForm.gender" placeholder="选择" class="min">
        <el-option label="男" value="M"></el-option>
        <el-option label="女" value="F"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="证件号码" prop="id_card">
      <el-input v-model="infoForm.id_card" class="mid"></el-input>
    </el-form-item>
    <br v-if="inline">
    <el-form-item label="学号" prop="student_id">
      <el-input v-model="infoForm.student_id" class="mid"></el-input>
    </el-form-item>
    <el-form-item prop="birth" label="生日">
      <el-date-picker type="date" placeholder="选择日期" v-model="infoForm.birth_date" class="mid"></el-date-picker>
    </el-form-item>
    <br v-if="inline">
    <el-form-item label="服装号码" prop="clothes_size">
      <el-select v-model="infoForm.clothes_size" placeholder="选择" class="min">
        <el-option label="XS" value="XS"></el-option>
        <el-option label="S" value="S"></el-option>
        <el-option label="M" value="M"></el-option>
        <el-option label="L" value="L"></el-option>
        <el-option label="XL" value="XL"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="移动电话" prop="cellphone_num">
      <el-input v-model="infoForm.cellphone_num" class="mid"></el-input>
    </el-form-item>
    <br v-if="inline">
    <el-form-item label="电子邮箱" prop="email">
      <el-input v-model="infoForm.email" class="mid"></el-input>
    </el-form-item>
    <el-form-item label="寝室" prop="dormitory">
      <el-input v-model="infoForm.dormitory" class="mid"></el-input>
    </el-form-item>
    <br v-if="inline">
    <el-form-item>
      <el-button type="primary" @click="submitForm">提交信息</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
  import ElInput from '../../../node_modules/element-ui/packages/input/src/input.vue'

  export default {
    components: {ElInput},
    data () {
      return {
        id: null,
        infoForm: {
          faculty: '',
          class_id: '',
          reading_degree: '',
          name: '',
          gender: '',
          id_card: '',
          student_id: '',
          birth_date: '',
          clothes_size: '',
          cellphone_num: '',
          email: '',
          dormitory: ''
        },
        rules: {
          name: [
            {required: true, message: '请输入名字'}
          ],
          student_id: [
//            {type: 'number', message: '年龄必须为数字值'},
            {required: true, message: '请输入学号'}
          ]
        }
      }
    },
    methods: {
      submitForm () {
//        this.$http({
//          method: 'GET',
//          url:''
//        })
        console.log(this.id)
        this.$http.post(
          'http://localhost:8000/api/user_info_submit/' + this.id,
          this.infoForm, {emulateJSON: true}
        ).then((response) => {
//          let res = JSON.parse(response.body)
          var res = response
          console.log('response', response)
          if (res.statusText === 'OK') {
            alert('已经提交表单')
          } else {
            alert('失败，请检查您输入')
          }
        })
        this.$emit('submit')
      },
      onSubmit () {
        console.log('submit!')
      },
      storeForm () {
        console.log('store')
        localStorage.setItem('submitform', JSON.stringify(this.form))
      }
    },
    props: {
      inline: Boolean,
      uid: Number
    },
    mounted:
      function () {
        if (this.uid) {
          this.id = this.uid
        } else {
          this.id = this.$route.params.uid
        }
        this.$http.get('http://localhost:8000/api/user_info_request/' + this.id).then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
//            this.dynamicValidateForm.name = res.list[0].fields.name
//            this.ruleForm.birth_date = ''
            this.infoForm = res.list[0].fields
          } else {
            this.$message.error('获取个人信息列表失败"')
            console.log(res['msg'])
          }
        })
      }
  }
</script>

<style scoped>
  .mid {
    width: 220px;
  }

  .min {
    width: 80px;
    margin-right: 140px;
  }
</style>

<template>
  <div id="app">
    <auth-component v-if="!isAuth" @handleAuth="handleAuth" />
    <div v-else>
      <p>Ви авторизовані</p>
    </div>
  </div>
</template>

<script>
import AuthComponent from './components/AuthComponent.vue'

export default {
  name: 'App',
  components: {
    AuthComponent
  },
  data(){
    return{
      isAuth: false
    }
  },
  methods:{
    handleAuth(){
      this.isAuth=true;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

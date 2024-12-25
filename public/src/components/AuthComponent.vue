<template>
  <div>
    <h2>Реєстрація</h2>
    <form @submit.prevent="register">
      <div>
        <label for="registerName">Ім'я:</label>
        <input type="text" id="registerName" v-model="registerName">
      </div>
      <div>
        <label for="registerAge">Вік:</label>
        <input type="text" id="registerAge" v-model="registerAge">
      </div>

      <button type="submit">
        Зареєструватися
      </button>
    </form>

        <h2>Авторизація</h2>
    <form @submit.prevent="login">
      <div>
        <label for="loginName">Ім'я:</label>
        <input type="text" id="loginName" v-model="loginName">
      </div>

      <button type="submit">
        Увійти
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'AuthComponent',
  data() {
    return {
      registerName: '',
      registerAge: '',
      loginName: ''
    }
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/users/', {
          name: this.registerName,
          age: this.registerAge
        });
        console.log("Register success: ", response.data);
      } catch (error) {
        console.error("Error registering user:", error);
        alert('Помилка реєстрації');
      }
    },

    async login() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/users/${this.loginName}`);
        if (response.data) {
          this.$emit('handleAuth');
        } else {
          alert('Користувач не знайдений');
        }
      } catch (error) {
        console.error("Error logging in:", error);
        alert('Помилка авторизації');
      }
    }
  }
}
</script>

<style>

</style>

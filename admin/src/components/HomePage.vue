<template>
  <div class="flex items-center justify-center h-screen">
    <h1 class="text-3xl font-bold text-center mb-6">Z-Hiring</h1>
    <p>Check our dashboard for different hiring assistants</p>
    <button><router-link to="/loginPage" class="no-underline text-black">Login</router-link></button>
    <p>Want to be a member? Sign up here</p>
    <div class="flex justify-center mb-4">
      <button><router-link to="/signupPage" class="no-underline text-black">Sign Up</router-link></button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  methods: {
    login() {
      // Redirect to login page
      this.$router.push({ name: 'loginPage' });
    },
    signUp() {
      // Redirect to sign up page
      this.$router.push({ name: 'signupPage' });
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 400px;
  border: 2px solid rgb(0, 0, 0);
  border-radius: 8px;
  padding: 20px;
}

button {
  padding: 10px 20px;
  background-color: #2aa8df;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #1935ec;
}

button:active {
  background-color: #5b1ed6;
}

.no-underline {
  text-decoration: none;
}

.text-white {
  color: rgb(255, 252, 252);
}
</style>

import { createApp } from 'vue';

const App = {
  data() {
    return {
      message: 'Welcome to the E-commerce Frontend!'
    };
  },
  template: `<div><h1>{{ message }}</h1></div>`
};

createApp(App).mount('#app');

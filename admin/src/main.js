import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

// Add all icons to the library so you can use it in your project
library.add(fas);

// Optionally, if you only need to import specific icons, you can do so like this:
import { faUser, faCog } from '@fortawesome/free-solid-svg-icons';
library.add(faUser, faCog);

const app = createApp(App);

// Register the FontAwesomeIcon component globally
app.component('font-awesome-icon', FontAwesomeIcon);

// Use Vue Router
app.use(router);

// Mount the app to the DOM
app.mount('#app');

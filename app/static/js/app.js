/* Add your Application JavaScript */
// 
/*
const Home = {   
  name: 'Home',   
  template: `      
    <div class="home">        
      <img src="/static/images/logo.png" alt="VueJS Logo">        
      <h1>{{ welcome }}</h1>      
    </div>      
  `,   
  data() {
    return {           
      welcome: 'Hello World! Welcome to VueJS'       
    }   
  }
};


const app = Vue.createApp({
  data() {
    return {
      welcome: 'Hello World! Welcome to VueJS'
    }
  },
  components: {    
    'home': Home,    
  }
});

app.component('app-header', {
  name: 'AppHeader',
  template: `
      <header>
          <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
            <a class="navbar-brand" href="#">VueJS App</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                  <router-link to="/" class="nav-link">Home</router-link>
                </li>
                <li class="nav-item">
                  <router-link to="/news" class="nav-link">News</router-link>
                </li>
              </ul>
            </div>
          </nav>
      </header>    
  `,
  data: function() {
    return {};
  }
});

app.component('app-footer', {
  name: 'AppFooter',
  template: `
      <footer>
          <div class="container">
              <p>Copyright &copy {{ year }} Flask Inc.</p>
          </div>
      </footer>
  `,
  data: function() {
      return {
          year: (new Date).getFullYear()
      }
  }
})

const router = VueRouter.createRouter({  
  history: VueRouter.createWebHistory(),  
  routes: [      
    { path: '/', component: Home },      
  ]
});

app.use(router)

app.mount('#app');
*/
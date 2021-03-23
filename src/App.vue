<template>
  <script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>

 <div id="app">
  <div class="outline">
      <nav class="main-nav">
       <div class="logo">
        {{ $route.name }}
       </div>
       <Burger></Burger>
      </nav>

      <router-view />
     <Sidebar>


       <ul class="sidebar-panel-nav">

         <li><router-link to="/">Home</router-link></li>
         <li><router-link to="/legalhistory">Legal History</router-link></li>
         <li><router-link to="/technicalhistory">Technical History</router-link></li>
          <li><router-link to="/scrapingprojects">Scraping Projects</router-link></li>
          <li><router-link to="/technicalaspects">Technical Aspects</router-link></li>

       </ul>
     </Sidebar>
  </div>
 </div>
</template>

<script>

</script>
<style>


html, body {
  height: 100%;
/*  overflow: hidden;
*/  margin: 0;
  padding: 0;
/*  background-color: white !important;*/
/*  background-color: #FFD662FF !important;
*/
}
/*html {
  height: 100%;
  overflow:hidden;
  background-color: #FFD662FF;
 }
body {
  padding: 0;
  margin: 0;
  width: 100%;
  min-height: 100%;
  background-color: #FFD662FF !important;
}
*/

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: white;
  padding-right: 5px;
  padding-left: 5px;

}
.outline{
  outline-style: solid;
  outline-color: black;
/*  outline-offset: 15px;
*/}
.logo {
  align-self: center;
  color: black;
  font-weight: bold;
  font-size: 35px;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
 }
 .main-nav {
  display: flex;
  justify-content: space-between;
  padding: 0.8rem 0.8rem;
  background-color: white;
  outline-style: solid;
  outline-color: black;

 }

 ul.sidebar-panel-nav {
   list-style-type: none;
 }

 ul.sidebar-panel-nav > li > a {
   color: black;
   text-decoration: none;
   font-size: 1.5rem;
   display: block;
   padding-bottom: 0.5em;
 }
</style>



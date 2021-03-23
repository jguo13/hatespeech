

<template>

<div class="navbar">
<section class="hero is-fullheight is-primary is-bold">
  <!-- Hero header: will stick at the top -->
  <div class="hero-head">
    <nav class="navbar">
      <div class="navbar-brand">


        <a class="navbar-item" href="/">
          <h3 class="headline">{{ $route.headline }}</h3>
        </a>
        <!--
    Using the v-on: directive to listen for the click event and toggle the data property showNav. Also, using the v-bind: directive to reactively update the class attribute 'is-active' based on the showNav property.
    -->
        <div class="navbar-burger" v-on:click="showNav = !showNav" v-bind:class="{ 'is-active' : showNav }">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
      <!--
    Using the v-bind: directive to reactively update the class attribute 'is-active' based on the showNav property.
    -->
      <div class="navbar-menu" v-bind:class="{ 'is-active' : showNav }">
        <div class="navbar-end">
          <a class="navbar-item" href="/about">
          <router-link to="/">Home</router-link> |

          </a>
          <a class="navbar-item" href="/path">
            <router-link to="/about">About</router-link> |
          </a>
          <a class="navbar-item" href="/blog">
        <router-link to="/profile">Profile</router-link>
          </a>
        </div>
      </div>
    </nav>
  </div>
  <!-- Hero content: will be in the middle -->
  <div class="hero-body">
    <div class="container has-text-centered">
    </div>
  </div>
</section>
</div>
<!--   <b-navbar toggleable type="dark" variant="dark" style=color:beige>
    <b-navbar-brand href="#">NavBar</b-navbar-brand>
    <b-navbar-toggle target="navbar-toggle-collapse">
      <template #default="{ expanded }">
        <b-icon v-if="expanded" icon="chevron-bar-up"></b-icon>
        <b-icon v-else icon="chevron-bar-down"></b-icon>
      </template>
    </b-navbar-toggle>

    <b-collapse id="navbar-toggle-collapse" is-nav>
      <b-navbar-nav class="ml-auto">

        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link> |
        <router-link to="/profile">Profile</router-link>


      </b-navbar-nav>
    </b-collapse>
  </b-navbar> -->
</template>

<script>

// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
// import "bulma/sass/utilities/all";
// import "bulma";
export default {
  name: "Navbar",
}

</script>

<style scoped>
/*.navbar-menu {
  float:right;
}
.headline{

}*/

.navbar-item {
  color:#4a4a4a !important;
}

.navbar {
  background: beige;
}
</style>
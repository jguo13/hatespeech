<template>


  <div>
	<div>
	<particles-bg type="cobweb" :bg="true" />


	</div>
  	<h3> prof page </h3>
  	<h4>{{$route.params.id}}</h4>

  </div>
</template>

<!-- <script>
// @ is an alias to /src

// export default {

// };
</script> -->

<style scoped>
 #particles-js{
        width: 100%;
        height: calc(100% - 100px);
                 position: absolute; 
    }

</style>
<template>
    <div>
      <h1>Add Movie</h1>
      <movie-form></movie-form>
    </div>
  </template>
  
  <script>
  import MovieForm from '@/components/MovieForm.vue';
  
  export default {
    components: {
      MovieForm
    }
  };
  </script>
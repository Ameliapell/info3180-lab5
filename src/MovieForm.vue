<template>
  <form @submit.prevent="saveMovie">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control" v-model="movie.title" />
    </div>
    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" class="form-control" v-model="movie.description"></textarea>
    </div>
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster</label>
      <input type="file" name="poster" class="form-control" @change="handleFileUpload" accept="image/*" />
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>
<script setup>
import { ref } from 'vue';

const movie = ref({
  title: '',
  description: '',
  poster: null
});

const saveMovie = () => {
  const formData = new FormData();
  formData.append('title', movie.value.title);
  formData.append('description', movie.value.description);
  formData.append('poster', movie.value.poster);

  fetch('/api/v1/movies', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      // Display a success message
      console.log(data);
    })
    .catch(error => {
      console.log(error);
    });
};
</script>

<script>
export default {
  data() {
    return {
      movie: {
        title: '',
        description: '',
        poster: null
      }
    };
  },
  methods: {
    saveMovie() {
      // Make AJAX request to the API route (endpoint) you created
      // Use the movie data from the 'movie' object in the request
      // Handle the response or any errors
    },
    handleFileUpload(event) {
      this.movie.poster = event.target.files[0];
    }
  }
};
</script>

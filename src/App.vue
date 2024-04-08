<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
</script>

<<template>
  <div>
    <h1>Movie Upload Form</h1>
    <movie-form></movie-form>
  </div>
</template>

<script>
import MovieForm from './components/MovieForm.vue';

export default {
  components: {
    MovieForm
  }
};
</script>
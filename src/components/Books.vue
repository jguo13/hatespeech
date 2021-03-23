<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Scrape</h1>
        <hr><br><br>

<alert :message=message v-if="showMessage"> 

</alert>


<div v-if='loadingStatus' class='loading-div'>
<vue-spinner />
</div>

<br>
  <b-form @submit="onTest" class="w-100">
  <button type="submit" class="btn btn-success btn-sm">Test</button>

</b-form>
<button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Scrape a Domain</button>
        <br><br>
<!--         <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Domain Scraped</th>
              <th scope="col">Length of Scrape</th>
              <th scope="col">Done?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table> -->
      </div>
    </div>
<b-modal ref="addBookModal"
         id="book-modal"
         title="Add a new book"
         hide-footer>
  <b-form @submit="onSubmit" @reset="onReset" class="w-100">
  <b-form-group id="form-title-group"
                label="Domain:"
                label-for="form-title-input">
      <b-form-input id="form-title-input"
                    type="text"
                    v-model="addBookForm.title"
                    required
                    placeholder="Enter Domain">
      </b-form-input>
    </b-form-group>
<!--     <b-form-group id="form-author-group"
                  label="Author:"
                  label-for="form-author-input">
        <b-form-input id="form-author-input"
                      type="text"
                      v-model="addBookForm.author"
                      required
                      placeholder="Enter author">
        </b-form-input>
      </b-form-group>
    <b-form-group id="form-read-group">
      <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
        <b-form-checkbox value="true">Read?</b-form-checkbox>
      </b-form-checkbox-group>
    </b-form-group> -->


    <b-button type="submit" variant="primary">Submit</b-button>
    <b-button type="reset" variant="danger">Reset</b-button>
  </b-form>
</b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import Spinner from 'vue-simple-spinner'

export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
      message: '',
      showMessage: false,
      ROOT_API: process.env.ROOT_API,
    };
  },
  components: {
    alert: Alert,
    vueSpinner: Spinner
  },
  computed: {
      loadingStatus () {
        return this.$store.getters.loadingStatus
      }
  },

  methods: {

    changed: function(event) {
      this.$store.commit('change', event.target.value)
    },
    getBooks() {
      const path = 'http://scrapingproject.example.com/books/books';
      // const path = 'http://flask-service:5000/books'
      // const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      const path = 'http://scrapingproject.example.com/books/books';

      // const path = 'http://flask-service:5000/books'
      // const path = 'http://localhost:5000/books';

      this.$store.commit('loadingStatus', true)
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Scrape Finished';
          this.showMessage = true;
          this.$store.commit('change', payload.title);
          this.$store.commit('loadingStatus', false)

        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    onTest(evt) {
      evt.preventDefault();
      
      // const path = `${this.ROOT_API}/books/ping`;
      const path = 'http://scrapingproject.example.com/books/ping'
      // const path = 'http://flask-service:5000/books/ping'
      // const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then(function (response) {
          // handle success
          console.log(response);
        })
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getBooks();
  },
};
</script>

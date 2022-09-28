<template>
  <div id="app">
    <h1 style="text-align:center;">Drogasil</h1>
    <div class="btn">
      <input type="text" name="" id="" placeholder="O que deseja encontrar" v-model="medicamentosNome">
      <button @click="getMedicamentos()">Buscar</button>
    </div>
    <table class="table">
      <thead>
      <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Indications</th>
        <th>AgainstIndications</th>
        <th>AdverseReactions</th>
        <th>Precautions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="medicamento in medicamentos" :key="medicamento.name">
        <td>{{ medicamento.name }}</td>
        <td>{{ medicamento.price }}</td>
        <td>{{ medicamento.indications }}</td>
        <td>{{ medicamento.againstIndications }}</td>
        <td>{{ medicamento.adverseReactions }}</td>
        <td>{{ medicamento.precautions }}</td>
      </tr>
    </tbody>
    </table>
   
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
      medicamentoNome: '',
      medicamentos: []
    }
  },
  
  methods: {
    async getMedicamentos(){
      var response = await fetch('http://127.0.0.1:8000/api/medicamentos/');
      this.medicamentos = await response.json();
    },
  },
  computed: {
    filterList(){
      return this.medicamentos.filter((medicamento)=>{
        return medicamento.name.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  }
}
</script>

<style>
  .btn {
    display: flex;
    flex-direction: column;
  }

  .btn input {
    padding: 1%;
    border-radius: 5px;
    border: 1px solid rgb(207, 205, 205);
    margin: 15px 0;
  }

  .btn button {
    background-color: rgb(31, 159, 31);
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 1%;
    font: 22px bold;
  }
</style>

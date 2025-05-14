<script lang="ts">
      let file: File | null = null;
      let query = "";
      let data: any = null; // Declare and initialize 'data'
      let searchResults = [];
      let isLoading = false;
      let sending = false;
      let search = '';

       async function handleFileUpload(event: { target: { files: any; }; }) {
            const selectedFiles = event.target.files;
            if (selectedFiles.length > 0) {
                  file = selectedFiles[0];
                  console.log('Selected file:', file);
            }
            const formData = new FormData();
            if (file) {
                  formData.append('file', file);
            } else {
                  console.error('No file selected');
            }
            try {
                  const response = await fetch('http://localhost:8000/uploadfile/', {
                  method: 'POST',
                  body: formData,
            });
            data = await response.json();
            console.log('Upload response:', data);
            }
            catch (error) {
                  console.error('Error uploading file:', error);
            }
            
      }

      async function handleQueryChange() {
            
            console.log('jkkkkkkkkkkkkkkkkkkkkkkkkkk:', query);


            sending = true;

            try {
                  const response = await fetch('http://localhost:8000/query/', {
                        method: 'POST',
                        headers: {
                              'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ query }),
                  });
                  data = await response.json();
                  console.log('Query response:', data);

                  query = "";
            } catch (error) {
                  console.error('Error sending query:', error);
            }
      }
      async function getData(){
            try{
                  const response = await fetch('http://localhost:8000/uploaddone/', {
                        method: 'GET',
                        headers: {
                              'Content-Type': 'application/json',
                        },
                  });
                  data = await response.json();
                  console.log('dataresponse:', data);
            } catch (error) {
                  console.error('Error sending query:', error);
            }
      }
      async function getresponse (){
            try{
                  const response = await fetch('http://localhost:8000/q/', {
                        method: 'GET',
                        headers: {
                              'Content-Type': 'application/json',
                        },
                  });
                  data = await response.json();
                  console.log('dataresponse:', data);
            } catch (error) {
                  console.error('Error sending query:', error);
            }
      }

      
      // async function handleSearch() {
      //       isLoading = true;
      //       sending = true;
      //       console.log('Searching for:', search);
      
      //       setTimeout(() => {
      //             searchResults = ['Result 1', 'Result 2', 'Result 3'];
      //             isLoading = false;
      //             sending = false;
      //       }, 2000);

      //       try {
      //             const response = await fetch('http://localhost:8000/search/', {
      //                   method: 'POST',
      //                   headers: {
      //                         'Content-Type': 'application/json',
      //                   },
      //                   body: JSON.stringify({ search }),
      //             });
      //             const data = await response.json();
      //             console.log('Search response:', data);
      //       } catch (error) {
      //             console.error('Error sending search:', error);
      //       }
      // }



       
</script>

<div class ="container">
      <div class="card"> 
            <!-- <div class="search">
                  <input class ="sqaure" type="text" placeholder="semantic search"  bind:value={search}/>
                  <button class="button" on:click={handleSearch}>🔍</button>    
            </div> -->
            <div>
                  <input type="file" class = "input-id" multiple on:change={handleFileUpload}/>
            </div>
            <div>
                  {#if data}
                        <div>
                              <pre>{JSON.stringify (data) }</pre>
                        </div>
                  {/if}
            </div>



            <div class = "input">
                  <input class="query" type="text" placeholder="Enter your query" bind:value={query} on:keydown={(event) => {if (event.key === "Enter") {handleQueryChange()}}}/>
                  <button class="circle"  on:click={handleQueryChange}> ⮝</button>
            </div>
               
      </div>
      
</div>

<style>
      .container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f0f2f5;
      }
  .card {
    text-align: center ;
    border: 1px solid #cccccc;
    padding: 16px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    height: 100%;
    width: 100%;
  }
 
.input-id {
      margin-top: 50px;
      margin-left: 100px; 
}
  /* . {
    background-color: #1890ff;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 10px;
    cursor: pointer;
    height: 40px;
      width: 100px;
  } */
 
  /* .primary-button:hover {
    background-color: #40a9ff;
  } */
  /* .text {
    text-align: center;
    margin-bottom: 16px;
  } */
 .input {
      position: relative;
      width: 100%;
      max-width: 600px;
      margin: 0 auto;
      margin-top: 500px;
      
}
.query {
      width: 100%;
  padding: 12px 48px 12px 16px;
  border-radius: 24px;
  border: 1px solid #ccc;
  font-size: 16px;
  outline: none;
  box-sizing: border-box;
}
.circle {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  background-color: #1890ff;
  color: white;
  border: none;
  padding: 8px 12px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 16px;
     
}

</style>
  

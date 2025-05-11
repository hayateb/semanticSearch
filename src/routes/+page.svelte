<script lang="ts">
       
</script>

<div class ="container">
      <div class="card"> 
            <div class="search">
                  <input class ="sqaure" type="text" placeholder="semantic search" />
                  <button class="button">🔍</button>    
            </div>
            <div>
                  <h3 class="text">Upload Your Files</h3>
                  <button class="primary-button">Browse</button>
            </div>
            <div class = "input">
                  <input class= "query" type = text placeholder="Enter your query" />
                  <button class="circle"> ⮝</button>
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
  .search {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin-left: auto;
}
.sqaure {
      
  width: 100%;
  padding: 10px 40px 10px 12px; /* padding-right for button space */
  border-radius: 20px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}
.button {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  background: #1890ff;
  border: none;
  cursor: pointer;
  font-size: 18px;
}

  .primary-button {
    background-color: #1890ff;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 10px;
    cursor: pointer;
    height: 40px;
      width: 100px;
  }
 
  .primary-button:hover {
    background-color: #40a9ff;
  }
  .text {
    text-align: center;
    margin-bottom: 16px;
  }
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
  

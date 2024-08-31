# Assignment Repository
Tried my best, had fun. Thanks for this assignment DaSH Labs! 
## Development Assignment

### Level 1

I mainly referred to the OpenAI's quickstart guides for this pretty simple code.
Just make sure you have set an OpenAI key as an environment variable before running it and have the OpenAI library installed
```
<bash>pip install openai
```
```
<bash>export OPENAI_API_KEY="your_api_key_here"
```

### Level 2
I used the basic HTTP sockets, used a 12 client - 1 server approach, each client responsible for one prompt and the rest is done as specified. 
To run the entire client-server code- 
```
./launch.sh
```

### Level 3

Make sure that docker-compose and docker are both installed to run this. Do set an OpenAI API key in the Server Dockerfile to run this. 

```
ENV OPENAI_API_KEY <your-openai-key>
```

To run simply navigate to
```
cd DaSH-Lab-Assignment-2024/DevelopmentAssignment/Level3
```
and run
```
docker-compose up --build 
```

## Project Assignment

### Level 1

List of Literature Review - 
+ "Fast Distributed Inference Serving for Large Language Models" (FastServe Paper)
+ "Attention is All You Need"
+ Distributed Systems Playlist by Chris Collohan
+ "Does Varying the BeeGFS Configuration Affect the I/O Performance of HPC Workloads?" 
+ Chapters 35-41, 48-50 from Operating Systems: Three Easy Pieces. (Read the Persistence Module)
Will try to read the Helix and Petals papers before the interview
  
  
 
### Level 2

Installed Pytorch,TensorFlow,HuggingFace's Transformer's library. To start using GPT-2 was simple, but initially it was generating the same sentence over and over again. Had to play around with settings of the generate() function (do_sample, top_k, top_p, temperature, etc.) to get a coherent prompt. 

### Level 3

Was not able to do Level 3 due to time constraints, but would love to attempt this some day :)


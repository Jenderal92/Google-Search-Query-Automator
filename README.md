# Google Search Query Automator

![Google-Search-Query-Automator Jenderal92](https://github.com/user-attachments/assets/9de7263f-4949-45c1-9032-6585bf36db9f)


**Google Search Query Automator** is an automation tool that leverages the **Google Custom Search API** to perform searches based on keywords and display the results. This tool allows users to automate the search process on Google, providing an easy way to search for information via API without having to access the web user interface directly. GQA can be used to retrieve search results in a structured format, showing titles, links, and snippets for each search result.

---

### **How to Use**
1. **Prepare API Key and CSE ID**:
   - **API Key**: You can obtain the API Key by registering at [Google Cloud Console](https://console.cloud.google.com/) and enabling the **Custom Search API**.
   - **CSE ID**: Create a **Custom Search Engine** at [Google Custom Search Engine](https://cse.google.com/cse/) and obtain its ID.

2. **Install Dependencies**:
   - Install the required Python libraries using pip:
     ```bash
     pip install requests
     ```

3. **Run the Program**:
   - Replace the `api_key` and `cse_id` variables with the values you obtained.
   - Run the program using the command:
     ```bash
     python2 file.py
     ```

4. **Enter Query and Number of Results**:
   - After running the script, you will be prompted to enter the search query and the number of results you want to display (1-10).

---

### **Tool Features**
1. **Search Automation**:
   - Uses Google Custom Search API to search for information based on a given keyword.
   
2. **Number of Results Configuration**:
   - Users can choose the number of search results to display, with a limit between 1 and 10 results.

3. **Search Based on Query**:
   - Users can input search keywords, which are then processed to retrieve relevant results.

4. **Clean Search Results Display**:
   - Displays search results in an easily readable format, including the title, link, and snippet text from the search results.

---

### **1. Getting API Key from Google Cloud Console**
To use the Google Custom Search API, you need to create a project in Google Cloud Console and enable the **Custom Search API**. Here are the steps:

#### **Steps to Obtain API Key:**
1. **Open Google Cloud Console**:
   - Visit [Google Cloud Console](https://console.cloud.google.com/).
   
2. **Create a New Project**:
   - Click the **Google Cloud Console** icon in the top left, then select **Create Project**.
   - Name the project as desired, then click **Create**.

3. **Enable Custom Search API**:
   - After the project is created, in the left panel, click **API & Services** > **Library**.
   - Search for **Custom Search API** in the search box.
   - Click **Google Custom Search API**, then click **Enable** to activate this API for your project.

4. **Get API Key**:
   - After enabling the API, click **Credentials** in the left panel.
   - Click **Create Credentials** and select **API Key**.
   - You will receive an API Key that you can use to make API requests.

5. **Note the API Key**:
   - After the API Key is generated, make sure to note it down as you will need to use it in your code.

### **2. Getting CSE ID (Custom Search Engine ID)**

To use **Custom Search Engine** (CSE) and get the **CSE ID**, you need to create a custom search engine through **Google Custom Search Engine**.

#### **Steps to Obtain CSE ID:**
1. **Open Google Custom Search Engine**:
   - Visit [Google Custom Search Engine](https://cse.google.com/cse/).

2. **Create a New Search Engine**:
   - Click **Add** to create a new search engine.
   - Choose **Sites to Search** and enter the domain or website you want to search (e.g., `example.com`). You can also choose to search the entire web.
   - Click **Create** to create the Custom Search Engine.

3. **Get CSE ID**:
   - After creating the Custom Search Engine, click on the **Control Panel** of the newly created search engine.
   - Under the **Details** section, you will see the **Search Engine ID** called **cx**.
   - Note down this **Search Engine ID**, as this is the **CSE ID** you will use in your code.

### **3. Adding API Key and CSE ID to Your Code**

Now that you have both the **API Key** and **CSE ID**, you can integrate them into the Python code you created. Replace the `api_key` and `cse_id` variables with the values you obtained:

```python
# Replace api_key and cse_id with the values you obtained
api_key = "YOUR_API_KEY"  # Insert your API Key here
cse_id = "YOUR_CSE_ID"    # Insert your CSE ID here
```

---

### **Summary**
1. **API Key**: Obtained through Google Cloud Console after enabling the **Custom Search API**.
2. **CSE ID**: Obtained after creating a Custom Search Engine at [Google Custom Search Engine](https://cse.google.com/cse/).


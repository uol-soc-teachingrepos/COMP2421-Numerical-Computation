# WS01 guide

Worksheet (not in this pack):
<https://uol-soc-teachingrepos.github.io/COMP2421-Numerical-Computation/ws/ws01.html>

KEY OBJECTIVE: can students open jupyter lab, import numpy as run simple cost? if not go to labs and ask for help

1. Check understand of content from last weeks lectures

	- matrices and vectors (addition, multiplication, scalar multiplication, dot product)
	- dot product/scalar product was done a bit quick at the end of the lecture

2. Ask if attempted worksheet

   - Have students been able to get jupyter lab running at all?
   - Recommend "regular second year lab" sessions for support in getting starter (the lab leaders have been given this worksheet)
   - mention "launch binder" button at top of worksheet

	 - this provides a web version of jupyter lab with the notebooks already available
	 - files are lost at the end of each session so "download to save before you leave"
	 - you can use this in tutorial so as to be able to use the university machines in each tutorial room

	**When opening jupyter notebook select "View -> Presentation Mode"**

3. Do a walk through of important features

	a. What are cells and how to execute? (inc cell types - markdown and code)
	b. Remember to restart kernel and run all before submission to make sure no hidden state
	c. Introduction to numpy https://uol-soc-teachingrepos.github.io/COMP2421-Numerical-Computation/ws/ws01.html#step-3-using-numpy

       - how to import
	   - how to make array
	   - how to ensure dtype=np.double
	   - indexing
	   - matrix addition, multiplication ("@" operator), dot product (np.dot)
	   - get students to tell you how to implement matrix multiplication:

		```python
		def matmul(A, B):
			assert A.shape[1] == B.shape[0]

			C = np.zeros((A.shape[0], B.shape[1]))
			rows, cols = C.shape

			for i in range(rows):
				for j in range(cols):
					for k in range(A.shape[1]):
						C[i][j] += A[i][k] * B[k][j]

			return C
		```

4. Do some examples of matrix multiplication and scalar product. Get students to do these on the board!
   (They need to know how to do this by hand)

const handleChange = (e) => {
    navigate('/allarticles', { state: e.target.value })
    setIsShow(false)

  }
  const handleSidebarMenu =(e)=>{
    navigate('/articletopics', { state: e.target.innerText })
    setIsShow(false)
  }
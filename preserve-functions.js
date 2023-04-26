const handleChange = (e) => {
    navigate('/allarticles', { state: e.target.value })
    setIsShow(false)

  }
  const handleSidebarMenu =(e)=>{
    navigate('/articletopics', { state: e.target.innerText })
    setIsShow(false)
  }


    // Construct the LinkedIn sharing URL
    const shareUrl = `https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(websiteUrl)}&title=${encodeURIComponent(websiteTitle)}`;
  
    // Open a new window to share the URL on LinkedIn
    window.open(shareUrl, '_blank');
  }
  
  // Share on Twitter
  function shareOnTwitter() {
    const articleUrl = window.location.href;
    const shareUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(articleUrl)}&text=${document.title}`;
    window.open(shareUrl, '_blank');
  }
  
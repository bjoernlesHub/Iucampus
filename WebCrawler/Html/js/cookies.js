(function(global, factory) {
    global.jscookie = factory();
})(this, function() {
  return {
      set: (name, value, days, attributes) => {
          let attr = [];
          let name_value = name + "=" + encodeURIComponent(value);
          attr.push(name_value);
		  attr.push("SameSite=None");
		  attr.push("secure");
          if (typeof days === "number") {
              let expires = "expires=" + new Date(Date.now() + 864E5 * days).toUTCString();
              attr.push(expires);
          }
          if (typeof attributes == 'object') {
              attributes.path = attributes.path == undefined ? "/" : attributes.path;
          } else {
              attributes = {
                  path: "/"
              };
          }
          for (let attribute_name in attributes) {
              if (attribute_name != "expires" || attribute_name != "max-age") {
                  let attr_name = attribute_name + "=" + attributes[attribute_name];
                  attr.push(attr_name);
              }
          }
          return document.cookie = attr.join("; ");
      },

      get: key => {
          let cookies = document.cookie.split('; ');
          let cookies_list_obj = {};
          for (let i = 0; i < cookies.length; i++) {
              let name_value = cookies[i].split('=');
              let name = name_value[0];
              let value = decodeURIComponent(name_value[1]);
			  //console.log(name+"="+value);
              cookies_list_obj[name] = value;
              if (key === name) {
                  break;
              }
          }
          if (key !== undefined) {
              return cookies_list_obj[key] ? cookies_list_obj[key] : null;
          } else {
              return Object.keys(cookies_list_obj).length === 0 ? null : cookies_list_obj;
          }
      },

      remove: (name, attributes) => {
          let attr = [];
          let name_value = name + "=";
          attr.push(name_value);
          if (typeof attributes == 'object') {
              attributes.path = attributes.path == undefined ? "/" : attributes.path;
          } else {
              attributes = {
                  path: "/"
              };
          }
          attributes.Expires = "Thu, 01 Jan 1970 00:00:01 GMT";
          for (let attribute_name in attributes) {
              if (attribute_name != "max-age") {
                  let attr_name = attribute_name + "=" + attributes[attribute_name];
                  attr.push(attr_name);
              }
          }
          return document.cookie = attr.join("; ");
      }
  };
});

		$("#btnSaveCookie").click(() => {
			//alert($("#website-select").val());
			jscookie.set("website-select",$("#website-select").val(),30);
			
			$("#inputarea :input").each(function(){
				var input = $(this);
				var name=input.attr('id');
				var value="";
				if(input.attr("type")=="checkbox")
				{
					value=input.is(':checked');				
				}
				else{
					value=input.val();
				}
				jscookie.set(name,value,30);
			$("#btnGetCookies").display="block";
			//alert("A cookie was setted");
			});
		})
		

		$("#btnGetCookies").click(() => {
			$("#website-select").val(jscookie.get("website-select"));
			$("#website-select").change();
			setTimeout(
			  function() 
			  {
				$("#inputarea :input").each(function(){
				var input = $(this);
				var name=input.attr('id');
				//console.log(jscookie.get(name));
				if(input.attr("type")=="checkbox")
				{
					input.checked = jscookie.get(name);				
				}
				else{
					input.val(jscookie.get(name));
				}
			});
			  }, 200);
		
		})
		
		if(jscookie.get("website-select")!=null && jscookie.get("website-select")!=""){
			$("#btnGetCookies").show();
			//alert("sollte sichtbar sein");
		}
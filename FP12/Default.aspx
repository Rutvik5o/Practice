<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
    <style type="text/css">
    .css1
    {
       color:green;
       background-color:white;
       border:2px solid blue;
    }
    
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <p>
        &nbsp;</p>
    <div>
    
    </div>
    <asp:Label ID="Label1"
     runat="server"
      Text="Label"
       CssClass="css1" 
      onmouseover="this.style.backgroundColor='pink';this.style.color='cyan';this.style.border='2px solid grey'" >
       </asp:Label>
    <p>
        &nbsp;</p>
    <p>
        &nbsp;</p>
    <p>
        &nbsp;</p>
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" 
        Text="Redirect on another page" />
    </form>
</body>
</html>

<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
    <style type="text/css">
    .style1
    {
      background-color:blue;
      color:Red;
      border: 2px solid black;
    }
    
    .style2
    {
    	background-color : Green;
    	color:Green;
    	border : 20px solid purple;
    }
        
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:Label ID="Label1" runat="server" Text="Text changes will be shown here"></asp:Label>
    
    </div>
    <p>
        &nbsp;</p>
    <asp:Button ID="Button1" runat="server" Text="Style1" onclick="Button1_Click" 
        style="height: 26px" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <asp:Button ID="Button2" runat="server" Text="Style2" onclick="Button2_Click" />
    </form>
</body>
</html>

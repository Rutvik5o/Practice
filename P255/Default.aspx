<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
</head>
<body>
    <form id="form1" runat="server">
    <p>
        Select State -&gt;&nbsp;
        <asp:DropDownList ID="DropDownList1" runat="server" AutoPostBack="True" 
            DataSourceID="AccessDataSource1" DataTextField="StateName" 
            DataValueField="StateCode" Width="80px">
        </asp:DropDownList>
        <asp:AccessDataSource ID="AccessDataSource1" runat="server" 
            DataFile="~/MSC.mdb" 
            SelectCommand="SELECT [StateCode], [StateName] FROM [State]">
        </asp:AccessDataSource>
    </p>
    <p>
        &nbsp;</p>
    <p>
        Select City -&gt;
        <asp:DropDownList ID="DropDownList2" runat="server" AutoPostBack="True" 
            DataSourceID="AccessDataSource2" DataTextField="CityName" 
            DataValueField="CityCode">
        </asp:DropDownList>
        <asp:AccessDataSource ID="AccessDataSource2" runat="server" 
            DataFile="~/MSC.mdb" 
            SelectCommand="SELECT [CityCode], [CityName], [StateCode] FROM [City] WHERE ([StateCode] = ?)">
            <SelectParameters>
                <asp:ControlParameter ControlID="DropDownList1" Name="StateCode" 
                    PropertyName="SelectedValue" Type="Int32" />
            </SelectParameters>
        </asp:AccessDataSource>
    </p>
    <p>
        &nbsp;</p>
    <p>
        <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="Submit" />
    </p>
    <div>
    
    </div>
    </form>
</body>
</html>
